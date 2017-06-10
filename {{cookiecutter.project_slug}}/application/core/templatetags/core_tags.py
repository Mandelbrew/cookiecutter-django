from django import template

register = template.Library()


# region Helpers

def get_wagtail_children_live_in_menu_all(root_page, active_page):
    """
    Recursively find all live pages that have attribute In Menu flipped on.

    :param root_page: The root_page page to start the search
    :param active_page: The page currently being requested
    :return: The filtered QuerySet of pages that are in the menu
    """
    menu_items = root_page.get_children().live().in_menu()

    for item in menu_items:
        item.active = item.url == active_page.url
        item.children = get_wagtail_children_live_in_menu_all(item, active_page)

    return menu_items


def get_wagtail_children_live_in_menu_top(root_page, active_page):
    """
    Find top live pages that have attribute In Menu flipped on.

    :param root_page: The root page to start the search
    :param active_page: The page currently being requested
    :return: The filtered QuerySet of pages that are in the menu
    """
    menu_items = root_page.get_children().live().in_menu()

    for item in menu_items:
        item.active = item.url == active_page.url
        item.children = item.get_children().live().in_menu()

    return menu_items


# endregion

# region Filters

@register.filter
def get_type(value):
    return type(value)


# endregion

# region Simple Tags


# endregion

# region Assignment Tags

@register.assignment_tag(takes_context=True)
def get_wagtail_all_menu_items(context, parent=None, caller=None):
    """
    Retrieves all menu items - all pages with In Menu flag turned on.

    :param context: used for automatic resolution ofcalling page and site's root page
    :param parent: the root page to start the search
    :param caller: the current active page being requested
    :return: dictionary tree with all pages in menu
    """
    call_page = caller if caller else context['page']
    root_page = parent if parent else context['request'].site.root_page
    return get_wagtail_children_live_in_menu_all(root_page, call_page)


@register.assignment_tag(takes_context=True)
def get_wagtail_top_menu_items(context, parent=None, caller=None):
    """
    Retrieves the top menu items - the immediate children of the parent page.

    :param context: used for automatic resolution ofcalling page and site's root page
    :param parent: the root page to start the search
    :param caller: the current active page being requested
    :return: dictionary tree with all pages in menu
    """
    call_page = caller if caller else context['page']
    root_page = parent if parent else context['request'].site.root_page
    return get_wagtail_children_live_in_menu_top(root_page, call_page)


@register.assignment_tag(takes_context=True)
def get_wagtail_root_page(context):
    """this returns a core.Page, not the implementation-specific model used
    so object-comparison to self will return false as objects would differ"""
    return context['request'].site.root_page

# endregion

# region Inclusion Tags

# endregion
