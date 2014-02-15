import itertools

def group_items_by_dates(items):
    """ 
    Returns a dictionary containing lists of items grouped by the month.
    """
    grouped_item_collection = {}
    
    def group_by_date_string(item):
        return item.date.strftime('%B %Y')
    
    for group, items in itertools.groupby(items, group_by_date_string):
        grouped_item_collection[group] = list(items)
            
    return grouped_item_collection
