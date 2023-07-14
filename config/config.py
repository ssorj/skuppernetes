import os

site.output_dir = "docs"

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
)

site_settings = html_table(props, class_="properties")

props = (
    ("Controller version", "1.2.3 (sha256:176f578ac5c437ea61e7b521ff3ef52b6405da11417476c49464dd654a3cafd2)"),
    ("Transport version", "2.3.4 (sha256:55da164dcf6fd69a2675c254339f51a3dfcbe9494b0d44f0e79936ac7aa8a83e)"),
    ("Created", "2 days ago"),
)

site_properties = html_table(props, class_="properties")

## Links

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value)

    return f"<td>{value}</td>"

headings = "Name", "Status", "Cost"

data = (
    ("warehouse", "OK", 1),
    ("headquarters", "Error: Unreachable", 2),
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
    ("storefront", 1, "15 minutes", "3 minutes ago", None),
    ("storefront-2", "None", "24 hours", "2 hours ago", None),
)

token_table = html_table(data, headings=headings, cell_fn=cell)

## Connectors

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value, href="connector/index.html")

    return f"<td>{value}</td>"

headings = "Name", "Routing key", "Pod selector", "Pod port"

data = (
    ("orders", "orders:8080", "app=orders", "8080"),
)

connector_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "orders"),
    ("Routing key", "orders:8080"),
    ("Pod selector", "app=orders"),
    ("Pod port", "8080"),
)

connector_settings = html_table(props, class_="properties")

props = (
    ("Created", "2 days ago"),
)

connector_properties = html_table(props, class_="properties")

## Listeners

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value, href="listener/index.html")

    return f"<td>{value}</td>"

headings = "Name", "Routing key", "Service name", "Service port"

data = (
    ("inventory", "inventory:8080", "inventory", "8080"),
    ("database", "database:5432", "database", "5432"),
    ("database-2", "database:8080", "database", "8080"),
)

listener_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "inventory"),
    ("Routing key", "inventory:8080"),
    ("Service name", "inventory"),
    ("Service port", "8080"),
)

listener_settings = html_table(props, class_="properties")

props = (
    ("Created", "2 days ago"),
)

listener_properties = html_table(props, class_="properties")
