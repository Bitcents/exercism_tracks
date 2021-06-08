package twofer

import "fmt"

// ShareWith should have a comment documenting it.
func ShareWith(name string) string {
	inputName := name
	if inputName == "" {
		inputName = "you"
	}
	message := fmt.Sprintf("One for %v, one for me.", inputName)
	return message
}
