from numbers import Number

def ml_pipeline(scores: dict, threshold: float) -> dict:
###Valdation of Inputs
    if not isinstance(scores, dict):
        raise TypeError("Input mut be dict")
    
    if len(scores) == 0:
        raise ValueError("Input must not be empty")

    if not isinstance(threshold, Number):
        raise ValueError("Value should be Number")
####Filteration of values
    cleaned = {}
    
    for key, value in scores.items():
        if isinstance(key, str) and isinstance(value, Number):
         cleaned[key] = value

        if len(cleaned) == 0:
            raise ValueError("Model not passsed this cleaning test")
        
###scale of values between 0 - 1

    values = list(cleaned.values())

    min_values = min(values)
    max_values = max(values)

    if min_values == max_values:
       raise ValueError("min value doesn't equal to max value")

    scaled = {}

    for key, value in cleaned.items():
       scaled_values = (value - min_values) / (max_values - min_values)
       scaled[key] = scaled_values

###Filtered values will pass from now on
    filtered = {}

    for key, value in scaled.items():
       if value >= threshold:
          filtered[key] = value ###scaled_values = values

###Best from filtered VINIT...find it
    if len(filtered) == 0:
     best_model = None
    else:
       best_key, best_value = next(iter(filtered.items()))

       for key, value in filtered.items():
          if value >= best_value:
             best_key = key
             best_value = value

       best_model = (best_key, best_value)

    return {
       "cleaned"   : cleaned,
       "scaled"    : scaled,
       "filtered"  : filtered,
       "best_model": best_model
    }


scores = {
   "A": 40,
   "B": 70,
   "C": 90,
   "D": 10
}

print(ml_pipeline(scores, 0.8))
