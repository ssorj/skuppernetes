import os

site_url = os.environ.get("SITE_URL", "")

def path_nav(page):
    separator = "<span class=\"path-separator\">&#8250;</span>"
    links = [x.replace("href=\"", f"href=\"{site_url}") for x in list(page.path_nav_links)[1:]]
    links = separator.join(links)

    return f"<nav class=\"path-nav\">{links}</nav>"

def html_link(content, href=None):
    if href is None:
        return f"<a>{content}</a>"
    else:
        return f"<a href=\"{href}\">{content}</a>"

def table_button(content, href=None):
    if href is None:
        return f"<a class=\"table-button\">{content}</a>"
    else:
        return f"<a class=\"table-button\" href=\"{href}\">{content}</a>"

## Site

props = (
    ("Name", "storefront"),
    ("Ingress", "None"),
    ("Console enabled?", "Yes"),
    ("Routers", 1),
    ("Router CPU request", 1.0),
    ("Router CPU limit", 1.0),
)

site_settings = html_table(props, class_="properties")

props = (
    ("Version", "1.2.3"),
    ("Created", "2 days ago"),
)

site_properties = html_table(props, class_="properties")

## Links

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value)

    return f"<td>{value}</td>"

headings = "Name", "Status", "Cost", "Created"

data = (
    ("warehouse", "OK", 1, "1/8/2020"),
    ("headquarters", "Error: Unreachable", 2, "3/15/2020"),
)

link_table = html_table(data, headings=headings, cell_fn=cell)

headings = "Name", "Created"

data = (
    ("delivery-truck-201", "10/18/2021"),
    ("delivery-truck-202", "11/8/2021"),
)

incoming_link_table = html_table(data, headings=headings)

## Tokens

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value)
    elif column_index == 4:
        value = table_button("Download")

    return f"<td>{value}</td>"

headings = "Name", "Use limit", "Expiry", "Created", "Actions"

data = (
    ("storefront-token-1", 1, "15 minutes", "3 minutes ago", None),
    ("storefront-token-2", "None", "24 hours", "2 hours ago", None),
)

token_table = html_table(data, headings=headings, cell_fn=cell)

## Provided services

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value, href="provided-service/index.html")

    return f"<td>{value}</td>"

headings = "Name", "Ports", "Workload", "Created"

data = (
    ("orders", "8080", "deployment/orders", "2 days ago"),
)

provided_service_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "orders"),
    ("Workload", "deployment/orders"),
    ("Publish not ready addresses?", "No"),
)

provided_service_settings = html_table(props, class_="properties")

props = (
    ("Created", "2 days ago"),
)

provided_service_properties = html_table(props, class_="properties")

headings = "Port", "Name", "Protocol", "Created"

data = (
    ("8080", "api",  "TCP", "2 days ago"),
)

provided_service_ports_table = html_table(data, headings=headings)

## Required services

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value, href="required-service/index.html")

    return f"<td>{value}</td>"

headings = "Name", "Ports", "Created"

data = (
    ("inventory", "8080", "2 days ago"),
    ("database", "5432, 8080", "2 days ago"),
)

required_service_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "inventory"),
    ("Publish not ready addresses?", "No"),
)

required_service_settings = html_table(props, class_="properties")

props = (
    ("Created", "2 days ago"),
)

required_service_properties = html_table(props, class_="properties")

headings = "Port", "Name", "Protocol", "Created"

data = (
    ("8080", "http",  "TCP", "2 days ago"),
)

required_service_ports_table = html_table(data, headings=headings)
