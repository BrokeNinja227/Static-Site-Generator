from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

    def block_to_block_type(block):
        lines = block.split('\n')
        if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
            return BlockType.HEADING
        elif block.startswith('```') and block.endswith('```'):
            return BlockType.CODE
        elif all(line.startswith('>') for line in lines):
            return BlockType.QUOTE
        elif all(line.startswith('- ') for line in lines):
            return BlockType.UNORDERED_LIST
        elif len(lines) > 0:
            is_ordered = True
            for i, line in enumerate(lines, 1):
                if not line.startswith(f"{i}. "):
                    is_ordered = False
                    break
            if is_ordered:
                return BlockType.ORDERED_LIST
        return BlockType.PARAGRAPH
