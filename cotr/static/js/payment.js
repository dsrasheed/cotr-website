(function() {
    'use strict';

    const stripe = Stripe('pk_test_hES8oRfDor764zdzV0ecdhUX');
    const elements = stripe.elements();
    
    var style = {
        base: {
            color: '#32325d',
            lineHeight: '24px',
            fontFamily: 'Lato, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '18px',
            ['::placeholder']: {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#fa755a',
            iconColor: '#fa755a'
        }
    };

    const card = elements.create('card', {style: style});
    card.mount('#card-element');

    const cardError = document.getElementById('card-error');
    card.addEventListener('change', function(e) {
        if (e.error)
            cardError.textContent = e.error.message;
        else
            cardError.textContent = '';
    });

    const quantity = document.getElementById('quantity-element');
    quantity.addEventListener('keydown', function(e) {
        var code = e.keyCode;
        if (code === 8 || code === 46)
            return;    
        e.preventDefault();

        var digit = Number(e.key);
        if (digit || digit === 0)
            this.value += e.key;
        
        // TODO: Placeholder not set when length is 0
        this.placeholder = !this.value.length ?  
            this.getAttribute('placeholder') :
            '';
    });

    function requiredFieldFilled(inputId) {
        var input = document.getElementById(inputId);
        var root = inputId.split('-')[0];
        var errorId = root + '-error';
        var errorElem = document.getElementById(errorId);

        if (!String(input.value).length) {
            errorElem.textContent = root.capitalize() + ' is required.';
            return false;
        } else {
            errorElem.textContent = '';
            return true;
        }
    }

    const payForm = document.getElementById('payment-form');
    payForm.addEventListener('submit', function(e) {
        e.preventDefault();
            
        if (!requiredFieldFilled('email-element') ||
            !requiredFieldFilled('quantity-element'))
            return;

        stripe.createToken(card).then(function(result) {
            if (result.error)
                cardError.textContent = result.error.message;
            else
                stripeTokenHandler(result.token);
        });

        function stripeTokenHandler(token) {
            var tokenInput = document.createElement('input');
            tokenInput.setAttribute('type','hidden');
            tokenInput.setAttribute('name', 'stripeToken');
            tokenInput.setAttribute('value', token);

            payForm.appendChild(tokenInput);
            payForm.submit();
        }
    });   
})();

