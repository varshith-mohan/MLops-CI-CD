# MLops-CI-CD
Continuous Integration (CI) in MLOps is the practice of automatically validating every change made to ML code, data pipelines, or configuration before it is merged into the main branch.

**Tools & Frameworks used for CI in MLOps**
<br>
### 1. CI Orchestration Tools
- GitHub Actions – YAML-based CI, very popular
- GitLab CI – Built-in CI/CD
- Jenkins – Highly customizable

**2. ML Experiment & Model Validation**

- MLflow – Metrics, experiments, model registry
- Weights & Biases
- DVC – Data + model versioning

### In MLOps, CI ensures that every code or data change is automatically tested for code quality, data consistency, and model performance. The pipeline validates data schemas, retrains the model on a small dataset, evaluates metrics against thresholds, and blocks merging if any validation fails.
