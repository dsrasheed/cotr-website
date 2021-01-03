# [Colors of the Region Event Website](http://cotr.herokuapp.com)

The event was held on June 30, 2017. This website provided info about the purpose of the event and enabled attenders to purchase tickets, print them, and have them verified when they arrived.

### Using the Ticket Purchase System

I use [Stripe](https://stripe.com/) to accept payments from cards. After the event ended, I didn't want the website to still accept payments from real cards, so I put my Stripe account in testing mode. The website will now only accept dummy card numbers. To see the ticket system in action, enter "4242 4242 4242 4242" and random numbers for the "MM/YY" and "CVC" fields. The website will send an email to your address containing the link to print your dummy tickets.
