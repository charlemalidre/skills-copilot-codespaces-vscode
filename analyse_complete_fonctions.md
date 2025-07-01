# Étude et Représentation Graphique de Fonctions

## Introduction

Ce document présente l'étude complète de trois fonctions dans un repère orthonormal (O; i⃗; j⃗) :

- **a)** f(x) = x⁴ - 2x² - 6
- **b)** f(x) = (x² - 1)/(4x + 5)  
- **f)** f(x) = (x² + 4x + 7)/(x² + x - 2)

---

## Fonction A: f(x) = x⁴ - 2x² - 6

### 1. Domaine de définition
**Df = ℝ** (ensemble des nombres réels)

Cette fonction polynomiale est définie pour toutes les valeurs réelles de x.

### 2. Étude des limites
- **lim f(x) quand x → +∞ = +∞**
- **lim f(x) quand x → -∞ = +∞**

La fonction tend vers l'infini positif aux deux extrémités, ce qui est caractéristique d'une fonction polynomiale de degré pair avec coefficient dominant positif.

### 3. Dérivées
- **f'(x) = 4x³ - 4x = 4x(x² - 1) = 4x(x-1)(x+1)**
- **f''(x) = 12x² - 4 = 4(3x² - 1)**

### 4. Étude du signe de f'(x)
f'(x) = 4x(x-1)(x+1) = 0 pour x = -1, 0, 1

- Pour x ∈ ]-∞, -1[ : f'(x) < 0 (fonction décroissante)
- Pour x ∈ ]-1, 0[ : f'(x) > 0 (fonction croissante)
- Pour x ∈ ]0, 1[ : f'(x) < 0 (fonction décroissante)  
- Pour x ∈ ]1, +∞[ : f'(x) > 0 (fonction croissante)

### 5. Points critiques
- **x = -1** : maximum local, f(-1) = 1 - 2 - 6 = -7
- **x = 0** : minimum local, f(0) = -6
- **x = 1** : maximum local, f(1) = 1 - 2 - 6 = -7

### 6. Concavité (étude de f''(x))
f''(x) = 4(3x² - 1) = 0 pour x = ±√(1/3) = ±√3/3

- Points d'inflexion en x = ±√3/3

---

## Fonction B: f(x) = (x² - 1)/(4x + 5)

### 1. Domaine de définition
**Df = ℝ \ {-5/4}**

La fonction est définie pour tous les réels sauf x = -5/4 où le dénominateur s'annule.

### 2. Étude des limites
- **lim f(x) quand x → +∞ = +∞**
- **lim f(x) quand x → -∞ = -∞**
- **lim f(x) quand x → (-5/4)⁻ = -∞**
- **lim f(x) quand x → (-5/4)⁺ = +∞**

### 3. Asymptotes
- **Asymptote verticale : x = -5/4 = -1.25**

Pour déterminer l'asymptote oblique, on effectue la division euclidienne :
f(x) = (x² - 1)/(4x + 5) = (1/4)x - 5/16 + (-81/16)/(4x + 5)

- **Asymptote oblique : y = (1/4)x - 5/16**

### 4. Dérivées
- **f'(x) = [2x(4x + 5) - 4(x² - 1)]/(4x + 5)² = (4x² + 10x + 4)/(4x + 5)²**
- **f''(x) = [expression complexe]**

### 5. Étude du signe de f'(x)
f'(x) = (4x² + 10x + 4)/(4x + 5)²

Le discriminant : Δ = 100 - 64 = 36 > 0
Racines : x₁ = (-10 - 6)/8 = -2 et x₂ = (-10 + 6)/8 = -1/2

- f'(x) > 0 pour x ∈ ]-∞, -2[ ∪ ]-1/2, +∞[ (fonction croissante)
- f'(x) < 0 pour x ∈ ]-2, -5/4[ ∪ ]-5/4, -1/2[ (fonction décroissante)

---

## Fonction F: f(x) = (x² + 4x + 7)/(x² + x - 2)

### 1. Domaine de définition
Pour trouver les valeurs interdites, on résout x² + x - 2 = 0
Δ = 1 + 8 = 9, donc x = (-1 ± 3)/2
Racines : x = -2 et x = 1

**Df = ℝ \ {-2, 1}**

### 2. Étude des limites
- **lim f(x) quand x → +∞ = 1**
- **lim f(x) quand x → -∞ = 1**
- **lim f(x) quand x → (-2)⁻ = +∞**
- **lim f(x) quand x → (-2)⁺ = -∞**
- **lim f(x) quand x → 1⁻ = -∞**
- **lim f(x) quand x → 1⁺ = +∞**

### 3. Asymptotes
- **Asymptotes verticales : x = -2 et x = 1**
- **Asymptote horizontale : y = 1**

L'asymptote horizontale y = 1 s'obtient en divisant les coefficients dominants : 1/1 = 1

### 4. Dérivée
En utilisant la règle du quotient :
f'(x) = [(2x + 4)(x² + x - 2) - (x² + 4x + 7)(2x + 1)] / (x² + x - 2)²

Après développement et simplification :
**f'(x) = (-3x² - 6x - 15) / (x² + x - 2)²**

### 5. Étude du signe de f'(x)
Le numérateur : -3x² - 6x - 15 = -3(x² + 2x + 5)
Le discriminant : Δ = 4 - 20 = -16 < 0

Comme le coefficient dominant est négatif et Δ < 0, le numérateur est toujours négatif.
Le dénominateur est toujours positif (carré).

**Donc f'(x) < 0** sur tout le domaine de définition : la fonction est strictement décroissante sur chaque intervalle de définition.

---

## Représentation graphique

Le fichier `analyse_fonctions.png` contient les représentations graphiques des trois fonctions avec :

- **Fonction A** : Courbe polynomiale en forme de "W" avec deux maxima locaux en (-1, -7) et (1, -7), et un minimum local en (0, -6)
- **Fonction B** : Hyperbole avec asymptote verticale x = -1.25 et asymptote oblique y = 0.25x - 0.3125
- **Fonction F** : Fonction rationnelle avec deux asymptotes verticales (x = -2 et x = 1) et une asymptote horizontale (y = 1)

## Tableau de variations

### Fonction A: f(x) = x⁴ - 2x² - 6
| x     | -∞  | -1  | 0   | 1   | +∞  |
|-------|-----|-----|-----|-----|-----|
| f'(x) | -   | 0   | +   | 0   | -   | 0 | + |
| f(x)  | +∞  | ↘   | -7  | ↗   | -6  | ↘ | -7 | ↗ | +∞ |

### Fonction B: f(x) = (x² - 1)/(4x + 5)
| x     | -∞  | -2    | -5/4 | -1/2  | +∞  |
|-------|-----|-------|------|-------|-----|
| f'(x) | +   | 0     | ‖    | 0     | +   |
| f(x)  | -∞  | ↗ 3/7 | ‖ AV | ↘ 3/2 | ↗   | +∞ |

### Fonction F: f(x) = (x² + 4x + 7)/(x² + x - 2)
| x     | -∞ | -2  | 1   | +∞ |
|-------|----|----|-----|-----|
| f'(x) | -  | ‖   | -   | ‖   | - |
| f(x)  | 1  | ↘  | ‖ AV | ↘ | ‖ AV | ↘ | 1 |

*AV = Asymptote Verticale*

---

## Conclusion

Cette étude complète des trois fonctions montre :

1. **Fonction A** : Polynôme de degré 4 avec comportement typique en "W"
2. **Fonction B** : Fonction rationnelle avec asymptote oblique
3. **Fonction F** : Fonction rationnelle avec asymptote horizontale et comportement strictement décroissant

Chaque fonction présente des caractéristiques distinctes qui sont clairement visibles sur leurs représentations graphiques respectives.