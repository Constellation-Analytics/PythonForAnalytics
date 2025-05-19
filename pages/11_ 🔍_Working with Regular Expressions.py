# -------------------------------------------------------------------
#                         Regular Expressions 
# -------------------------------------------------------------------
import streamlit as st
st.header("🔍 Working with Regular Expressions")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Introduction to regex patterns.
- Regex Special Characters
- Searching for patterns in strings.
- Extracting and substituting text using regex.

"""
)
st.subheader("Introduction to regex patterns")
st.markdown("""
- **[abc]**: Matches any single character that is either *a*, *b*, or *c*. The square brackets define a character class, which matches one character that is any of those listed.

- **[^abc]**: Matches any single character that is *not* *a*, *b*, or *c*. The caret (^) negates the character class, meaning any character except the listed ones.

- **[a-z]**: Matches any single lowercase letter from *a* to *z* (inclusive). It’s a shorthand for the range of characters in the alphabet.

- **[A-Z]**: Matches any single uppercase letter from *A* to *Z* (inclusive).

- **[0-9]**: Matches any single digit from *0* to *9*. This represents a digit range.

- **[a-zA-Z]**: Matches any single letter, either lowercase (*a-z*) or uppercase (*A-Z*).

- **[\\d]**: Matches any single digit. Equivalent to `[0-9]`. It is a shorthand for digits.

- **[\\D]**: Matches any single non-digit character. Equivalent to `[^0-9]`. It will match anything except digits.

- **[\\w]**: Matches any single alphanumeric character (letters, digits, or underscore). Equivalent to `[a-zA-Z0-9_]`. It’s shorthand for word characters, which include letters, digits, and the underscore.

- **[\\W]**: Matches any single non-alphanumeric character. Equivalent to `[^a-zA-Z0-9_]`. It will match any character that is not a letter, digit, or underscore.

- **[\\s]**: Matches any whitespace character (spaces, tabs, newlines, etc.). It includes characters like spaces (`' '`), tabs (`'\\t'`), and newlines (`'\\n'`).

- **[\\S]**: Matches any non-whitespace character. This is the opposite of `\\s` and matches everything that is not a space, tab, newline, etc.

- **[\\b]**: Matches a word boundary, i.e., the position where a word character is next to a non-word character (like spaces, punctuation). For example, it matches between `"word "` and `" word"`.

- **[\\B]**: Matches a non-word boundary. This is the opposite of `\\b`, meaning it matches any position where there is no word boundary (between two word characters or between two non-word characters).

- **[\\Z]**: Matches the end of a string. It is useful for ensuring that the match occurs right at the end of the string, not just at the end of the current line.
""")

st.subheader("Regex Special Characters")
st.markdown("""
- **[ ] (square brackets)**: Defines a character class, matching any single character within the brackets. 

- **\\ (backslash)**: Used for escaping metacharacters (e.g., `\\.`, `\\*`, `\\[`, etc.), allowing them to be matched literally. 

- **"." (dot)**: Matches any single character except a newline. 

- **^ (caret)**: Anchors the regex at the start of the string. 

- **$ (dollar sign)**: Anchors the regex at the end of the string. 

- ***(asterisk)**: Matches 0 or more occurrences of the preceding character or group. 

- **+ (plus)**: Matches 1 or more occurrences of the preceding character or group. 

- **? (question mark)**: Matches 0 or 1 occurrence of the preceding character or group. 

- **{ } (curly braces)**: Specifies an exact number or range of occurrences:
  - `{n}`: Exactly *n* occurrences. For example, `a{3}` matches "aaa".
  - `{n,}`: At least *n* occurrences. For example, `a{2,}` matches "aa", "aaa", and so on.
  - `{n,m}`: Between *n* and *m* occurrences (inclusive). For example, `a{2,4}` matches "aa", "aaa", or "aaaa".

- **| (pipe)**: Acts as a logical OR. 

- **`()` (parentheses)**: Used to group parts of a regex for structure or to capture matched content:
  - **Grouping**: Parentheses group patterns, allowing operators like `+` or `|` to apply to the entire group.  
     *Example: `(abc)+` matches one or more occurrences of "abc".*
  - **Capturing Groups**: By default, parentheses store the matched content for later use (e.g., as `group(1)`).  
     *Example: `(dog|cat)` matches "dog" or "cat" and captures the match.*
  - **Non-Capturing Groups**: Use `(?:...)` to group patterns without saving matched content.  
     *Example: `((?:dog|cat) park)` matches "dog park" or "cat park" without capturing "dog" or "cat".*
""")


st.subheader("Basic Regex Patterns")
st.code(
"""
import re

# A sample text to search
text = "The rain in Spain falls mainly in the plain."

# Find all occurrences of 'ain'
pattern = r"ain"
matches = re.findall(pattern, text)
print("Matches:", matches)

# Output: Matches: ['ain', 'ain', 'ain']
"""
    )

st.subheader("Using Special Characters")
st.code(
"""
import re

# Sample text with digits
text = "My phone number is 123-456-7890."

# Find all digits
pattern = r"\d"
matches = re.findall(pattern, text)
print("Digits:", matches)

# Output: Digits: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Find all numbers
pattern = r"\d+"
matches = re.findall(pattern, text)
print("Numbers:", matches)

# Output: Numbers: ['123', '456', '7890']
"""
    )

st.subheader("Searching and Matching Patterns")
st.code(
"""
import re

# Sample text
text = "Hello World!"

# Check if the text starts with 'Hello'
pattern = r"^Hello"
match = re.search(pattern, text)
if match:
    print("Found:", match.group())
else:
    print("Not found")

# Output: Found: Hello
"""
    )

st.subheader("Substituting Text with Regex")
st.code(
"""
import re

# Sample text
text = "I love apples! Apples are my favorite fruit."

# Substitute 'apples' with 'bananas'
pattern = r"apples"
new_text = re.sub(pattern, "bananas", text, flags=re.IGNORECASE)
print(new_text)

# Output: I love bananas! Bananas are my favorite fruit.
"""
    )

st.subheader("Using Regex for Data Validation")
st.code(
"""
import re

# Sample email addresses
emails = ["user@example.com", "invalid-email", "user.name@domain.co"]

# Pattern to match a valid email
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Validate emails
for email in emails:
    if re.match(pattern, email):
        print(f"Valid: {email}")
    else:
        print(f"Invalid: {email}")

# Output:
# Valid: user@example.com
# Invalid: invalid-email
# Valid: user.name@domain.co
"""
    )
