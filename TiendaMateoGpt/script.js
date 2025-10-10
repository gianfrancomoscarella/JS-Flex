// script.js
export function inicializarTienda() {
    const productListDiv = document.getElementById("product-list");
    const cartCountSpan = document.getElementById("cart-count");
    const viewCartBtn = document.getElementById('view-cart-btn');

    if (!productListDiv || !cartCountSpan || !viewCartBtn) {
        console.warn("⚠️ Elementos de la tienda no encontrados todavía.");
        return;
    }

    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Actualiza el contador del carrito
    function updateCartCount() {
        cartCountSpan.textContent = cart.reduce((acc, item) => acc + item.quantity, 0);
    }

    // Agregar producto al carrito
    function addToCart(product) {
        const existingProduct = cart.find(item => item.id === product.id);
        if (existingProduct) {
            existingProduct.quantity += 1;
        } else {
            cart.push({ ...product, quantity: 1 });
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartCount();
        Toastify({
            text: `${product.name} agregado al carrito`,
            duration: 2500,
            gravity: 'top',
            position: 'right',
            backgroundColor: 'linear-gradient(to right, #00b09b, #96c93d)',
        }).showToast();
    }

    // Mostrar productos
    function displayProducts(products) {
        productListDiv.innerHTML = '';
        products.forEach(product => {
            const card = document.createElement('div');
            card.classList.add('product-card');
            card.innerHTML = `
                <img src="${product.image}" alt="${product.name}" />
                <h3>${product.name}</h3>
                <p>Precio: $${product.precio}</p>
                <button data-id="${product.id}">Agregar al carrito</button>
            `;
            productListDiv.appendChild(card);
        });

        document.querySelectorAll(".product-card button").forEach(button => {
            button.addEventListener("click", (evt) => {
                const id = parseInt(evt.target.dataset.id);
                const productToAdd = products.find(item => item.id === id);
                if (productToAdd) addToCart(productToAdd);
            });
        });
    }

    // Cargar productos desde JSON
    async function fetchProducts() {
        try {
            const res = await fetch('productos.json');
            if (!res.ok) throw new Error("Error en la respuesta de la API");
            const products = await res.json();
            displayProducts(products);
        } catch (error) {
            console.error("Error fetching products:", error);
        }
    }

    // Eliminar un producto del carrito
    function removeFromCart(id) {
        cart = cart.filter(item => item.id !== id);
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartCount();
    }

    // 🧹 Vaciar completamente el carrito
    function clearCart() {
        Swal.fire({
            title: '¿Vaciar carrito?',
            text: 'Se eliminarán todos los productos del carrito.',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Sí, vaciar',
            cancelButtonText: 'Cancelar',
        }).then((result) => {
            if (result.isConfirmed) {
                cart = [];
                localStorage.removeItem('cart');
                updateCartCount();
                Swal.fire({
                    icon: 'success',
                    title: 'Carrito vacío',
                    text: 'Se eliminaron todos los productos.',
                    timer: 2000,
                    showConfirmButton: false
                });
            }
        });
    }

    // Mostrar el carrito completo
    function showCart() {
        if (cart.length === 0) {
            Swal.fire({
                icon: 'info',
                title: "Carrito vacío",
                text: "Aún no has agregado productos al carrito",
            });
            return;
        }

        let html = '<ul style="list-style:none; padding:0;">';
        let total = 0;

        cart.forEach(item => {
            const itemTotal = item.precio * item.quantity;
            total += itemTotal;
            html += `
                <li>
                    <span>${item.name} x ${item.quantity}</span>
                    <span>$${itemTotal.toFixed(2)}</span>
                    <button data-id="${item.id}" class="remove-from-cart-btn">❌</button>
                </li>
            `;
        });

        // Total + botón de vaciar carrito
        html += `
            </ul>
            <p style="font-weight:bold; font-size:1.2rem; text-align:right; margin-top:20px;">
                Total: $${total.toFixed(2)}
            </p>
            <div style="text-align:right; margin-top:1rem;">
                <button id="clear-cart-btn" style="
                    background-color:#dc3545;
                    color:white;
                    border:none;
                    padding:0.5rem 1rem;
                    border-radius:5px;
                    cursor:pointer;
                ">🗑️ Vaciar carrito</button>
            </div>
        `;

        Swal.fire({
            title: "Tu Carrito de Compras",
            html,
            width: 600,
            showCancelButton: true,
            confirmButtonText: "Finalizar Compra",
            cancelButtonText: "Seguir Comprando",
            didOpen: () => {
                // Botones para eliminar productos individuales
                document.querySelectorAll(".remove-from-cart-btn").forEach(btn => {
                    btn.addEventListener("click", (evt) => {
                        const id = parseInt(evt.target.dataset.id);
                        removeFromCart(id);
                        showCart(); // refrescar
                    });
                });

                // Botón para vaciar carrito completo
                const clearBtn = document.getElementById("clear-cart-btn");
                if (clearBtn) clearBtn.addEventListener("click", clearCart);
            },
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire({
                    icon: "success",
                    title: "Compra realizada",
                    text: "¡Gracias por tu compra!",
                });
                cart = [];
                localStorage.removeItem("cart");
                updateCartCount();
            }
        });
    }

    // Inicialización
    viewCartBtn.addEventListener("click", showCart);
    fetchProducts();
    updateCartCount();
}
