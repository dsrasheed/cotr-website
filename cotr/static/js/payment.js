(function() {
    'use strict';

    const stripe = Stripe('pk_live_OkudCaCShkC5BQ52FxRIrZej');
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
    card.mount('#card');

    const cardError = document.getElementById('card-error');
    card.addEventListener('change', function(e) {
        if (e.error)
            cardError.textContent = e.error.message;
        else
            cardError.textContent = '';
    });

    const quantity = document.getElementById('quantity');
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

    function isFieldFilled(inputId) {
        return true;   
    }

    const ticketForm = document.getElementById('ticket-form');
    ticketForm.addEventListener('submit', function(e) {
        e.preventDefault();

        if (!isFieldFilled('email') ||
            !isFieldFilled('quantity'))
            return;

        stripe.createToken(card).then(function(result) {
            if (result.error)
                cardError.textContent = result.error.message;
            else
                stripeTokenHandler(result.token);
        });

        function stripeTokenHandler(token) {
            var tokenInput = document.getElementById('stripeToken');
            console.log(token);
            tokenInput.setAttribute('value', token.id)

            ticketForm.submit();
        }
    });   
})();
