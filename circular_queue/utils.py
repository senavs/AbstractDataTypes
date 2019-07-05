def next_position(pos, max_size):
    return (pos + 1) % max_size

def prev_position(pos, max_size):
    return (pos - 1 + max_size) % max_size
