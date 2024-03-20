document.getElementById('reservation-doctor').addEventListener('change', function() {
  // Panggil fungsi untuk memperbarui harga
  updatePriceOptions();
});

function updatePriceOptions() {
  // Dapatkan elemen dokter yang dipilih
  var selectedDoctor = document.getElementById('reservation-doctor').value;

  // Dapatkan elemen select harga
  var priceSelect = document.getElementById('reservation-price');

  // Hapus opsi harga yang ada
  priceSelect.innerHTML = "";

  // Loop melalui data harga dan tambahkan opsi yang sesuai dengan dokter yang dipilih
  {% for price_data in data['price'] %}
      if ("{{ price_data['specialist'] }}" === selectedDoctor) {
          var option = document.createElement("option");
          option.value = "{{ price_data['price'] }}";
          option.text = "{{ price_data['price'] }}";
          priceSelect.add(option);
      }
  {% endfor %}
}