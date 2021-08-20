package twofer

import "fmt"

// ShareWith is as simple function that takes
// a string, ideally a name, as its parameter
// and returns a greeting of type string. The greeting
// is of the form "One for {string}, one for me",
// where {string} can either be the parameter string
// or the word "you" if an empty string ("") is passed.
func ShareWith(name string) string {
	// If empty string is passed, change name to "you."
	if name == "" {
		name = "you"
	}
	return fmt.Sprintf("One for %s, one for me.", name)
}
