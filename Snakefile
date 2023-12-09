rule prepare:
    output:
        "data/car.data"
    shell:
        "scripts/prepare_data.py"

rule profile:
    input:
        "data/car.data"
    output:
        "profiling/report.html"
    shell:
        "scripts/profiles.py"

rule anaylze:
    input:
        "data/car.csv"
    output:
        "data/car.csv"
    shell:
        "scripts/analysis.py"