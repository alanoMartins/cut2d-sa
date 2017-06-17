# cut2d-sa

For the [Himmelblau's function][1] the output of cut2d-sa is a 5-tuple:
(iteration number, temperature, function value, x, y).

To get the file with output to plot run:

```
$ ./cut2d-sa > ent
```

To plot the file run:
```
$ ./temperature-plotter.py < ent
```

[1]: https://en.wikipedia.org/wiki/Himmelblau%27s_function
