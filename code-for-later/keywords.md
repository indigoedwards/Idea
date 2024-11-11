## job keywords
- only allowed one job keyword
- valid values assemble, find, plot-potential

```
job : assemble          OR
job : find              OR
job : plot-potential
```

## xgrid keywords
- all required
- xgrid-min, xgrid-max, xgrid-points
- xgrid-min and xgrid-max can be floats
- xgrid-points must be an integer greater than 0
```
xgrid-min : -5          AND
xgrid-max : 5           AND
xgrid-points : 150
```

## file path keywords
- can be absolute path (recommended?)
- can be relative path (might be buggy)
- path-output
    - path for general outputs (not including filename)
    - if path-state or path-graph not specified, they default to this directory
- path-state
    - directory for saving state files
- path-graph
    - directory for saving graphs (for gifs?)
- will create folders if they don't currently exist

## something keywords


## output keywords

