fetch('http://backend-service/api/products')
  .then(response => response.json())
  .then(products => {
    const list = document.getElementById('product-list');
    products.forEach(p => {
      const item = document.createElement('li');
      item.textContent = `${p.name} - $${p.price}`;
      list.appendChild(item);
    });
  });
