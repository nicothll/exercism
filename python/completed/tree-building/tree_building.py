from dataclasses import dataclass, field


@dataclass
class Record:
    """A class representing a single record in a tree.

    Attributes:
        record_id (int): The ID of the record.
        parent_id (int): The ID of the parent record.
    """

    record_id: int
    parent_id: int


@dataclass
class Node:
    """A class representing a node in a tree.

    Attributes:
        node_id (int): The ID of the node.
        children (list, optional): A list of child nodes.
    """

    node_id: int
    children: list = field(default_factory=list)


def BuildTree(records: list[Record]) -> Node:
    """Builds a tree of nodes from a list of Record objects.

    Args:
        records (list[Record]): A list of Record objects to build the tree from.

    Raises:
        ValueError: If any of the following occurs:
        - Node parent_id is greater than its record_id.
        - Record id is invalid or out of order.
        - Only the root node should have equal record and parent id.
        - Node parent_id is greater than its record_id.

    Returns:
        Node: The root node of the tree.

    Example Usage:
        >>> records = [Record(record_id=1, parent_id=0), Record(record_id=2, parent_id=1)]
        >>> root_tree = BuildTree(records)
    """
    if not records:
        return None

    ordered_records = sorted(records, key=lambda x: x.record_id)
    root_record = ordered_records.pop(0)

    if root_record.parent_id > 0:
        raise ValueError("Node parent_id should be smaller than it's record_id.")
    elif root_record.record_id > 0:
        raise ValueError("Record id is invalid or out of order.")

    nodes = [Node(root_record.record_id)]

    for idx, record in enumerate(ordered_records):
        if record.record_id != idx + 1:
            raise ValueError("Record id is invalid or out of order.")
        if record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")
        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")

        parent_node = nodes[record.parent_id]
        node = Node(record.record_id)
        parent_node.children.append(node)
        nodes.append(node)

    return nodes[0]
