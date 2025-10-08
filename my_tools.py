# ------------------
# my_tools.py
# ------------------

# Tool 1: A function to get data from a custom API or database
def get_customer_info(customer_id: int) -> dict:
    """
    Retrieves a customer's personal information (name, email, and address) 
    from the internal CRM system using their unique integer ID. 
    Use this tool when the user asks for contact details.
    """
    if customer_id == 101:
        return {"id": 101, "name": "Alice Johnson", "email": "alice@example.com", "address": "123 Main St"}
    elif customer_id == 102:
        return {"id": 102, "name": "Bob Smith", "email": "bob@test.com", "address": "456 Oak Ave"}
    else:
        return {"error": "Customer not found"}

# Tool 2: A function that performs an action, like sending a notification
def send_internal_alert(priority: str, message: str) -> str:
    """
    Sends a high-priority alert to the internal operations team's dashboard. 
    The priority must be 'HIGH', 'MEDIUM', or 'LOW'. 
    The message should summarize the user's request for action.
    """
    if priority.upper() in ["HIGH", "MEDIUM", "LOW"]:
        # Logic to integrate with your internal system (e.g., Slack, PagerDuty)
        print(f"*** Internal Alert Sent - Priority: {priority.upper()} - Message: {message} ***")
        return f"Alert with priority {priority} successfully dispatched."
    else:
        return "Error: Invalid priority level provided."