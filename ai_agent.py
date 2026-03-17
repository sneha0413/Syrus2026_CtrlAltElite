def ai_reasoning(ticket, code):

    ticket = ticket.lower()

    # CART
    if "cart" in ticket or "checkout" in ticket:
        return """
Root Cause:
The system does not validate whether the cart is empty before checkout.

Fix:
if(cart.length === 0){
    return res.status(400).json({error:"Cart is empty"})
}
"""

    # LOGIN
    elif "login" in ticket or "email" in ticket:
        return """
Root Cause:
Email comparison is case-sensitive causing login failures.

Fix:
email = email.toLowerCase()
storedEmail = storedEmail.toLowerCase()
"""

    # PAYMENT
    elif "payment" in ticket:
        return """
Root Cause:
Payment status is not validated before processing.

Fix:
if(payment.status !== "success"){
    return res.status(400).json({error:"Payment failed"})
}
"""

    # ORDER
    elif "order" in ticket:
        return """
Root Cause:
Order validation is missing or incomplete.

Fix:
if(!order){
    return res.status(404).json({error:"Order not found"})
}
"""

    # PASSWORD
    elif "password" in ticket:
        return """
Root Cause:
Password is stored without hashing.

Fix:
const bcrypt = require('bcrypt')
password = await bcrypt.hash(password, 10)
"""

    # 🔥 SMART FALLBACK (IMPORTANT)
    else:
        return f"""
Root Cause:
The issue appears to be a general validation or logical error based on the incident description:
"{ticket}"

Fix:
Add proper input validation, error handling, and logging in the affected module.
Check for null values, invalid inputs, and missing conditions.
"""