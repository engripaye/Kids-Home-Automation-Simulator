const devicesDiv = document.getElementById("devices");

async function loadDevices() {
    const res = await fetch("http://127.0.0.1:8000/devices/");
    const devices = await res.json();
    devicesDiv.innerHTML = "";
    devices.forEach(device => {
        const div = document.createElement("div");
        div.className = `device ${device.state ? 'on' : ''}`;
        div.innerHTML = `<h3>${device.name}</h3>
                         <p>Type: ${device.type}</p>
                         <p>State: ${device.state ? 'ON' : 'OFF'}</p>
                         <button onclick="toggleDevice(${device.id})">Toggle</button>`;
        devicesDiv.appendChild(div);
    });
}

async function toggleDevice(id) {
    await fetch(`http://127.0.0.1:8000/devices/${id}/toggle`, { method: "POST" });
    loadDevices();
}

loadDevices();
