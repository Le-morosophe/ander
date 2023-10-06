(function($) {
	"use strict"

	// Mobile Nav toggle
	$('.menu-toggle > a').on('click', function (e) {
		e.preventDefault();
		$('#responsive-nav').toggleClass('active');
	})

	// Fix cart dropdown from closing
	$('.cart-dropdown').on('click', function (e) {
		e.stopPropagation();
	});
    
	/////////////////////////////////////////

	// Products Slick
	$('.products-slick').each(function() {
		var $this = $(this),
				$nav = $this.attr('data-nav');

		$this.slick({
			slidesToShow: 4,
			slidesToScroll: 1,
			autoplay: true,
			infinite: true,
			speed: 300,
			dots: false,
			arrows: true,
			appendArrows: $nav ? $nav : false,
			responsive: [{
	        breakpoint: 991,
	        settings: {
	          slidesToShow: 2,
	          slidesToScroll: 1,
	        }
	      },
	      {
	        breakpoint: 480,
	        settings: {
	          slidesToShow: 1,
	          slidesToScroll: 1,
	        }
	      },
	    ]
		});
	});

	// Products Widget Slick
	$('.products-widget-slick').each(function() {
		var $this = $(this),
				$nav = $this.attr('data-nav');

		$this.slick({
			infinite: true,
			autoplay: true,
			speed: 300,
			dots: false,
			arrows: true,
			appendArrows: $nav ? $nav : false,
		});
	});

	/////////////////////////////////////////

	// Product Main img Slick
	$('#product-main-img').slick({
    infinite: true,
    speed: 300,
    dots: false,
    arrows: true,
    fade: true,
    asNavFor: '#product-imgs',
  });

	// Product imgs Slick
  $('#product-imgs').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true,
    centerMode: true,
    focusOnSelect: true,
		centerPadding: 0,
		vertical: true,
    asNavFor: '#product-main-img',
		responsive: [{
        breakpoint: 991,
        settings: {
					vertical: false,
					arrows: false,
					dots: true,
        }
      },
    ]
  });

	// Product img zoom
	var zoomMainProduct = document.getElementById('product-main-img');
	if (zoomMainProduct) {
		$('#product-main-img .product-preview').zoom();
	}

	/////////////////////////////////////////

	// Input number
	$('.input-number').each(function() {
		var $this = $(this),
		$input = $this.find('input[type="number"]'),
		up = $this.find('.qty-up'),
		down = $this.find('.qty-down');

		down.on('click', function () {
			var value = parseInt($input.val()) - 1;
			value = value < 1 ? 1 : value;
			$input.val(value);
			$input.change();
			updatePriceSlider($this , value)
		})

		up.on('click', function () {
			var value = parseInt($input.val()) + 1;
			$input.val(value);
			$input.change();
			updatePriceSlider($this , value)
		})
	});

	var priceInputMax = document.getElementById('price-max'),
			priceInputMin = document.getElementById('price-min');

	priceInputMax.addEventListener('change', function(){
		updatePriceSlider($(this).parent() , this.value)
	});

	priceInputMin.addEventListener('change', function(){
		updatePriceSlider($(this).parent() , this.value)
	});

	function updatePriceSlider(elem , value) {
		if ( elem.hasClass('price-min') ) {
			console.log('min')
			priceSlider.noUiSlider.set([value, null]);
		} else if ( elem.hasClass('price-max')) {
			console.log('max')
			priceSlider.noUiSlider.set([null, value]);
		}
	}

	// Price Slider
	var priceSlider = document.getElementById('price-slider');
	if (priceSlider) {
		noUiSlider.create(priceSlider, {
			start: [1, 999],
			connect: true,
			step: 1,
			range: {
				'min': 1,
				'max': 999
			}
		});

		priceSlider.noUiSlider.on('update', function( values, handle ) {
			var value = values[handle];
			handle ? priceInputMax.value = value : priceInputMin.value = value
		});
	}

})(jQuery);


$(document).ready(function() {
	$('.add-to-cart-btn').click(function(e) {
	  e.preventDefault();
	  // Récupérer les informations du produit à partir du bouton cliqué
	  var productId = $(this).data('product-id');
	  var productName = $(this).data('product-name');
	  var productPrice = $(this).data('product-price');
	  // Vérifier si le produit est déjà dans le panier
	  var cartData = localStorage.getItem('cart');
	  var cart = cartData ? JSON.parse(cartData) : {};
	  if (cart[productId]) {
		// Le produit est déjà dans le panier, augmenter la quantité
		cart[productId].quantity += 1;
	  } else {
		// Le produit n'est pas encore dans le panier, l'ajouter
		cart[productId] = {
		  name: productName,
		  price: productPrice,
		  quantity: 1
		};
	  }
	  // Mettre à jour le panier dans le stockage local
	  localStorage.setItem('cart', JSON.stringify(cart));
	  // Mettre à jour l'affichage du panier
	  updateCartCount();
	});
	function updateCartCount() {
	  var cartData = localStorage.getItem('cart');
	  var cart = cartData ? JSON.parse(cartData) : {};
	  var cartCount = Object.keys(cart).length;
	  var cartCountElement = document.getElementById('cart-count');
	  if (cartCountElement) {
		cartCountElement.innerHTML = cartCount;
	  }
	}
	// Mettre à jour l'affichage du panier lors du chargement de la page
	updateCartCount();
  });


  var categorySelect = document.getElementById("category-select");
  // Ajoutez un écouteur d'événements pour l'événement de changement
  categorySelect.addEventListener("change", function() {
	// Obtenez la valeur de l'option sélectionnée
	var selectedCategory = categorySelect.value;
	// Redirigez vers la page de la catégorie sélectionnée
	if (selectedCategory !== "0") {
	  window.location.href = "/category_products/" + selectedCategory + "/";
	}
  });  

