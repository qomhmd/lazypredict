import shap

class SHAPExplainer:
    """
    SHAPExplainer for interpreting model predictions using SHAP values.

    This class provides methods for explaining individual predictions and
    obtaining global feature importance using SHAP.

    Attributes
    ----------
    model : object
        The model to be explained.

    Methods
    -------
    explain(X):
        Compute SHAP values for the provided data.
    plot_summary(shap_values, X):
        Plot a SHAP summary plot.
    """

    def __init__(self, model, data=None):
        """
        Parameters
        ----------
        model : object
            A trained model compatible with SHAP explainers.
        data : DataFrame, optional
            Sample data used to create the masker for SHAP. Required for models
            that are not directly compatible with SHAP (like LinearRegression).
        """
        self.model = model
        if data is not None:
            self.explainer = shap.Explainer(self.model, shap.maskers.Independent(data))
        else:
            self.explainer = shap.Explainer(self.model)

    def explain(self, X):
        """
        Compute SHAP values for the provided data.

        Parameters
        ----------
        X : DataFrame
            Input data for which SHAP values are computed.

        Returns
        -------
        array-like
            SHAP values for each feature in the input data.
        """
        return self.explainer(X)

    def plot_summary(self, shap_values, X):
        """
        Plot a SHAP summary plot.

        Parameters
        ----------
        shap_values : array-like
            SHAP values for the input data.
        X : DataFrame
            Input data used for plotting feature importance.
        """
        shap.summary_plot(shap_values, X)
