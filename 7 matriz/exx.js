//aplicaçao para conseguirmos conexao com o servidor para disponibiliozar o mapa opensource
function reverseGeocode(lat, lng) {
  const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}&zoom=18&addressdetails=1`;
  fetch(url, {
    headers: {
      'Accept': 'application/json'
    }
  })
    .then(response => response.json())
    .then(data => {
      const display = data.display_name || 'Endereço não disponível';
      setResult(`Latitude: ${lat.toFixed(6)}<br>Longitude: ${lng.toFixed(6)}<br>${display}`, 'success');
    })
    .catch(() => {
      setResult(`Latitude: ${lat.toFixed(6)}<br>Longitude: ${lng.toFixed(6)}<br>Não foi possível obter o endereço.`, 'success');
    });
}

function obterLocalizacao() {
  if (!navigator.geolocation) {
    setResult('Seu navegador não suporta geolocalização.', 'error');
    return;
  }

  setResult('Obtendo localização...');
  getLocationBtn.disabled = true;

  navigator.geolocation.getCurrentPosition(
    position => {
      const lat = position.coords.latitude;
      const lng = position.coords.longitude;

      initMap(lat, lng);
      reverseGeocode(lat, lng);
      getLocationBtn.disabled = false;
    },
    error => {
      getLocationBtn.disabled = false;
      const message = error.code === 1
        ? 'Permissão negada. Ative a localização no navegador.'
        : 'Não foi possível obter sua localização.';
      setResult(message, 'error');
    }
  );
}

async function searchAddress() {
  const query = searchInput.value.trim();

  if (!query) {
    setResult('Digite um endereço ou cidade para pesquisar.', 'error');
    return;
  }

  setResult('Pesquisando endereço...');

  try {
    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&limit=1`;
    const response = await fetch(url);
    const data = await response.json();

    if (!data.length) {
      setResult('Nenhum resultado encontrado.', 'error');
      return;
    }

    const lat = parseFloat(data[0].lat);
    const lng = parseFloat(data[0].lon);
    initMap(lat, lng);
    setResult(`Resultado: ${data[0].display_name}<br>Latitude: ${lat.toFixed(6)}<br>Longitude: ${lng.toFixed(6)}`, 'success');
  } catch (error) {
    setResult('Erro ao pesquisar o endereço.', 'error');
  }
}

getLocationBtn.addEventListener('click', obterLocalizacao);
searchBtn.addEventListener('click', searchAddress);
searchInput.addEventListener('keydown', event => {
  if (event.key === 'Enter') {
    searchAddress();
  }
});