# Py pandoc include code
Python filter for pandoc to replace the original `pandoc-include-code` that is no longer supported (https://github.com/owickstrom/pandoc-include-code).
`py-pandoc-include-code` is a valid python package, thus you can install it simply with:

```bash
pip install git+https://github.com/veneres/py-pandoc-include-code.git
```
At the moment, the provides only two ways of including code:

- Whole file
- Snippet

The examples belows assume to have a file called `main.c` in the same directory of your markdown source:

```
// start snippet solution
#include <stdio.h>
#include <stdbool.h>

int foo() {
    printf("My snippet\n");
}
// end snippet solution


int main(int argc, char *argv[]) {

}
```

## Whole file inclusion

To include an entire file into your markdown, you can use:

    ```{.c include=main.c}

    ```

## Snippet inclusion

To include only part of your code between delimited by a tag such as `solution`, you need to use two special comments, 
following the template below.

```c
// start snippet solution
    
    <my snippet of code>
   
// end snippet solution
```
*Note*: the filter will match exactly the pattern `// start snippet <my-tag>` and `// end snippet <my-tag>`, 
including the white spaces.

Going back to the previous example, you can include the snippet `solution` in your markdown with: 

    ```{.c include=main.c snippet=solution}

    ```