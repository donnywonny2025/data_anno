let localDataDump = [];
let lastCount = 0;

const feedContainer = document.getElementById('feed-container');
const emptyState = document.getElementById('empty-state');
const syncStatus = document.getElementById('sync-status');
const clearBtn = document.getElementById('clearBtn');

async function pollLog() {
    try {
        const response = await fetch('/war_room/TASK_LOG/live_session.json?' + new Date().getTime());
        if (!response.ok) throw new Error('API unreachable');
        
        const data = await response.json();
        
        if (data.length === 0 && lastCount > 0) {
            feedContainer.innerHTML = '';
            feedContainer.appendChild(emptyState);
            emptyState.style.display = 'block';
            lastCount = 0;
        }
        
        if (data.length > lastCount) {
            if (emptyState) emptyState.style.display = 'none';
            for (let i = lastCount; i < data.length; i++) {
                appendNode(data[i]);
            }
            lastCount = data.length;
        }
        
        syncStatus.textContent = 'SYNC: OK';
        syncStatus.style.color = 'var(--text-secondary)';
        
    } catch (e) {
        console.error("Polling error", e);
        syncStatus.textContent = 'SYNC: ERR_NO_CONN';
        syncStatus.style.color = '#ff4444';
    }
    
    setTimeout(pollLog, 1500); 
}

function appendNode(item) {
    const node = document.createElement('div');
    node.className = 'feed-item';
    
    const d = item.timestamp ? new Date(item.timestamp) : new Date();
    // Millisecond-precision timestamp for a technical feel
    const timeString = d.toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute:'2-digit', second:'2-digit' }) + '.' + d.getMilliseconds().toString().padStart(3, '0');
    
    let parsedHTML = '';
    try {
        parsedHTML = marked.parse(item.extracted_text || '*No text extracted*');
    } catch (e) {
        parsedHTML = (item.extracted_text || '').replace(/\n/g, '<br/>');
    }
    
    node.innerHTML = `
        <div class="feed-meta">
            <span class="timestamp">${timeString}</span>
        </div>
        <div class="feed-content">
            <div class="feed-image">
                <a href="/${item.image_path}" target="_blank">
                    <img src="/${item.image_path}" alt="Captured context" onerror="this.src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxyZWN0IHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9IiMxODE5MUIiLz48dGV4dCB4PSI1MCUiIHk9IjUwJSIgZmlsbD0iIzkwOTI5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSI+SU1HX0VSUjwvdGV4dD48L3N2Zz4='"/>
                </a>
            </div>
            <div class="feed-text markdown-body">
                ${parsedHTML}
            </div>
        </div>
    `;
    
    // Insert newest at the top
    const firstReal = Array.from(feedContainer.children).find(el => el.id !== 'empty-state');
    if (firstReal) {
        feedContainer.insertBefore(node, firstReal);
    } else {
        feedContainer.appendChild(node);
    }
}

clearBtn.addEventListener('click', async () => {
    if (!confirm("Confirm purge of current session logs?")) return;
    try {
        const res = await fetch('/api/clear', { method: 'POST' });
        if (res.ok) {
            lastCount = 0;
            feedContainer.innerHTML = '';
            feedContainer.appendChild(emptyState);
            emptyState.style.display = 'block';
        }
    } catch(e) {
        alert("System error: Purge failed.");
    }
});

pollLog();


let currentProject = null;
const intPanel = document.getElementById('intelligence-panel');
const projectLabel = document.getElementById('active-project-label');
const scaffoldPanel = document.getElementById('scaffold-panel');

async function pollIntelligence() {
    try {
        const ptrRes = await fetch('/war_room/TASK_LOG/active_project.json?' + new Date().getTime());
        if (!ptrRes.ok) return;
        const config = await ptrRes.json();
        
        if (config.active_project && config.active_project !== currentProject) {
            currentProject = config.active_project;
            projectLabel.textContent = 'PROJECT: ' + currentProject;
            
            // Fetch the new project markdown
            const mdRes = await fetch('/war_room/RESEARCH/' + currentProject + '_rules.md?' + new Date().getTime());
            if (mdRes.ok) {
                const mdText = await mdRes.text();
                intPanel.innerHTML = marked.parse(mdText);
            } else {
                intPanel.innerHTML = '<div class="empty-state"><h3>// WAITING FOR RULE COMPILATION</h3></div>';
            }
        } else if (config.active_project === currentProject) {
            // Re-fetch to see if rules updated
            const mdRes = await fetch('/war_room/RESEARCH/' + currentProject + '_rules.md?' + new Date().getTime());
            if (mdRes.ok) {
                const mdText = await mdRes.text();
                intPanel.innerHTML = marked.parse(mdText);
            }
        }
    } catch(e) {
        console.error('Intelligence poll error', e);
    }
    setTimeout(pollIntelligence, 2000);
}
pollIntelligence();

async function pollScaffold() {
    try {
        const res = await fetch('/war_room/TASK_LOG/live_flight_plan.md?' + new Date().getTime());
        if (res.ok) {
            const mdText = await res.text();
            scaffoldPanel.innerHTML = marked.parse(mdText);
        }
    } catch(e) {
        console.error('Scaffold poll error', e);
    }
    setTimeout(pollScaffold, 1000); // Fast 1-second polling for live feel
}
pollScaffold();

let currentDashboardVersion = null;
async function pollDashboardVersion() {
    try {
        const verRes = await fetch('/war_room/TASK_LOG/dashboard_version.txt?' + new Date().getTime());
        if (verRes.ok) {
            const versionStr = await verRes.text();
            if (currentDashboardVersion === null) {
                currentDashboardVersion = versionStr.trim();
            } else if (currentDashboardVersion !== versionStr.trim()) {
                console.log("Dashboard version changed. Triggering silent background reload.");
                window.location.reload(true);
            }
        }
    } catch(e) {}
    setTimeout(pollDashboardVersion, 3000);
}
pollDashboardVersion();

const fcStatus = document.getElementById('fc-status');
async function pollMCPStatus() {
    try {
        const res = await fetch('/war_room/TASK_LOG/mcp_status.json?' + new Date().getTime());
        if (res.ok) {
            const statusData = await res.json();
            if (statusData.firecrawl === "ONLINE") {
                fcStatus.textContent = 'FC_MCP: ONLINE';
                fcStatus.style.color = '#00FF00'; // Green for operational
            } else {
                fcStatus.textContent = 'FC_MCP: OFFLINE';
                fcStatus.style.color = '#ff4444'; // Red for offline
            }
        }
    } catch(e) {
        fcStatus.textContent = 'FC_MCP: ERR';
        fcStatus.style.color = '#ff4444';
    }
    setTimeout(pollMCPStatus, 3000);
}
pollMCPStatus();
