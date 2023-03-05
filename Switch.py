match a:
    case 'a':
        print("Hello")
    case 'b':
        print("World")
    case 'ab':
        print("A")
    
    
    def number_to_string(agrument):
	match agrument:
		case 0:
			return "zero"
		case 1:
			return "one"
		case 2:
			return "two"


if __name__ = "__main__":
	agrument = 0
	number_to_string(agrument)
