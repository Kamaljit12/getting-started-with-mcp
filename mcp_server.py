# ------------------
# mcp_server.py
# ------------------
from mcp.server.fastmcp import FastMCP
from my_tools import get_customer_info, send_internal_alert
import argparse
import sys


SERVER_PORT = 8888 
# 1. Initialize the MCP Server
# Give your server a unique name for identification
# 1. Initialize the MCP Server
mcp_server = FastMCP(
    name="EnterpriseCustomerService", 
    port=SERVER_PORT,  # Use the variable here
    host="0.0.0.0"
)

# 2. Add (Register) the tools using a decorator or function call
@mcp_server.tool()
def get_customer_info_tool(customer_id: int) -> dict:
    """
    Retrieves a customer's personal information (name, email, and address) 
    from the internal CRM system using their unique integer ID. 
    Use this tool when the user asks for contact details.
    """
    return get_customer_info(customer_id)

# You can also register the tool directly without a decorator if needed
mcp_server.add_tool(send_internal_alert) 

# 3. Run the Server
if __name__ == "__main__":
    # Use the variable to print the port
    print(f"Starting MCP Server on port {SERVER_PORT}...") 
    
    # This line should now be on line 32 or later
    mcp_server.run() 