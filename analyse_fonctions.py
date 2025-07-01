import numpy as np
import matplotlib
matplotlib.use('Agg')  # Backend non-interactif pour environnement sans affichage
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import sympy as sp
from sympy import symbols, diff, limit, oo, solve, factor, simplify
import warnings
warnings.filterwarnings('ignore')

# Configuration matplotlib pour un affichage français
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (15, 12)

class AnalyseurFonction:
    def __init__(self, fonction_str, nom):
        self.nom = nom
        self.fonction_str = fonction_str
        self.x = symbols('x')
        self.fonction_sym = sp.sympify(fonction_str)
        
    def analyser_domaine(self):
        """Analyser le domaine de définition"""
        denominateur = sp.denom(self.fonction_sym)
        if denominateur != 1:
            # Trouver les valeurs interdites
            valeurs_interdites = solve(denominateur, self.x)
            return valeurs_interdites
        return "ℝ (tous les réels)"
    
    def calculer_limites(self):
        """Calculer les limites importantes"""
        limites = {}
        
        # Limites en ±∞
        try:
            limites['x→+∞'] = limit(self.fonction_sym, self.x, oo)
            limites['x→-∞'] = limit(self.fonction_sym, self.x, -oo)
        except:
            limites['x→+∞'] = "Non définie"
            limites['x→-∞'] = "Non définie"
        
        # Limites aux points de discontinuité
        valeurs_interdites = self.analyser_domaine()
        if valeurs_interdites != "ℝ (tous les réels)":
            for val in valeurs_interdites:
                try:
                    if val.is_real:
                        limites[f'x→{val}⁻'] = limit(self.fonction_sym, self.x, val, '-')
                        limites[f'x→{val}⁺'] = limit(self.fonction_sym, self.x, val, '+')
                except:
                    pass
        
        return limites
    
    def calculer_derivee(self):
        """Calculer la dérivée première"""
        return diff(self.fonction_sym, self.x)
    
    def calculer_derivee_seconde(self):
        """Calculer la dérivée seconde"""
        return diff(self.fonction_sym, self.x, 2)
    
    def trouver_asymptotes(self):
        """Trouver les asymptotes"""
        asymptotes = {}
        
        # Asymptotes verticales
        valeurs_interdites = self.analyser_domaine()
        if valeurs_interdites != "ℝ (tous les réels)":
            asymptotes['verticales'] = [float(val) for val in valeurs_interdites if val.is_real]
        
        # Asymptotes horizontales
        lim_inf_pos = limit(self.fonction_sym, self.x, oo)
        lim_inf_neg = limit(self.fonction_sym, self.x, -oo)
        
        if lim_inf_pos.is_finite:
            asymptotes['horizontale_+∞'] = float(lim_inf_pos)
        if lim_inf_neg.is_finite:
            asymptotes['horizontale_-∞'] = float(lim_inf_neg)
        
        # Asymptotes obliques (si pas d'asymptote horizontale)
        if not lim_inf_pos.is_finite and lim_inf_pos != oo and lim_inf_pos != -oo:
            try:
                a = limit(self.fonction_sym / self.x, self.x, oo)
                if a.is_finite and a != 0:
                    b = limit(self.fonction_sym - a * self.x, self.x, oo)
                    if b.is_finite:
                        asymptotes['oblique'] = (float(a), float(b))
            except:
                pass
        
        return asymptotes
    
    def evaluer_fonction(self, x_vals):
        """Évaluer la fonction pour les valeurs données"""
        func_lambdified = sp.lambdify(self.x, self.fonction_sym, 'numpy')
        try:
            return func_lambdified(x_vals)
        except:
            # Gérer les divisions par zéro
            y_vals = []
            for x_val in x_vals:
                try:
                    y_val = func_lambdified(x_val)
                    if np.isfinite(y_val):
                        y_vals.append(y_val)
                    else:
                        y_vals.append(np.nan)
                except:
                    y_vals.append(np.nan)
            return np.array(y_vals)

def analyser_et_tracer():
    """Analyser et tracer les trois fonctions"""
    
    # Définition des fonctions
    fonctions = [
        ("x**4 - 2*x**2 - 6", "f(x) = x⁴ - 2x² - 6"),
        ("(x**2 - 1)/(4*x + 5)", "f(x) = (x² - 1)/(4x + 5)"),
        ("(x**2 + 4*x + 7)/(x**2 + x - 2)", "f(x) = (x² + 4x + 7)/(x² + x - 2)")
    ]
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    axes = axes.flatten()
    
    # Analyse détaillée pour chaque fonction
    for i, (func_str, nom) in enumerate(fonctions):
        print(f"\n{'='*60}")
        print(f"ANALYSE DE LA FONCTION {chr(97+i).upper()}: {nom}")
        print(f"{'='*60}")
        
        analyseur = AnalyseurFonction(func_str, nom)
        
        # Domaine de définition
        domaine = analyseur.analyser_domaine()
        print(f"\n1. DOMAINE DE DÉFINITION:")
        if domaine == "ℝ (tous les réels)":
            print(f"   Df = ℝ")
        else:
            print(f"   Df = ℝ \\ {{{', '.join([str(val) for val in domaine])}}}")
        
        # Limites
        limites = analyseur.calculer_limites()
        print(f"\n2. LIMITES:")
        for point, valeur in limites.items():
            print(f"   lim f(x) quand {point} = {valeur}")
        
        # Dérivées
        derivee = analyseur.calculer_derivee()
        derivee_seconde = analyseur.calculer_derivee_seconde()
        print(f"\n3. DÉRIVÉES:")
        print(f"   f'(x) = {derivee}")
        print(f"   f''(x) = {derivee_seconde}")
        
        # Asymptotes
        asymptotes = analyseur.trouver_asymptotes()
        print(f"\n4. ASYMPTOTES:")
        if 'verticales' in asymptotes:
            for av in asymptotes['verticales']:
                print(f"   Asymptote verticale: x = {av}")
        if 'horizontale_+∞' in asymptotes:
            print(f"   Asymptote horizontale (x→+∞): y = {asymptotes['horizontale_+∞']}")
        if 'horizontale_-∞' in asymptotes:
            print(f"   Asymptote horizontale (x→-∞): y = {asymptotes['horizontale_-∞']}")
        if 'oblique' in asymptotes:
            a, b = asymptotes['oblique']
            print(f"   Asymptote oblique: y = {a}x + {b}")
        
        # Tracé du graphique
        ax = axes[i]
        
        # Déterminer l'intervalle de tracé selon la fonction
        if i == 0:  # Fonction polynomiale
            x_vals = np.linspace(-3, 3, 1000)
        elif i == 1:  # Fonction rationnelle avec asymptote en x = -5/4
            x_vals = np.concatenate([
                np.linspace(-4, -1.26, 500),
                np.linspace(-1.24, 4, 500)
            ])
        else:  # Fonction rationnelle avec asymptotes en x = -2 et x = 1
            x_vals = np.concatenate([
                np.linspace(-5, -2.05, 300),
                np.linspace(-1.95, 0.95, 400),
                np.linspace(1.05, 5, 300)
            ])
        
        y_vals = analyseur.evaluer_fonction(x_vals)
        
        # Masquer les valeurs infinies pour un meilleur affichage
        mask = np.isfinite(y_vals)
        x_clean = x_vals[mask]
        y_clean = y_vals[mask]
        
        # Limiter l'affichage vertical pour une meilleure visualisation
        if i == 0:
            y_lim = (-10, 10)
        else:
            y_lim = (-15, 15)
        
        mask_y = (y_clean >= y_lim[0]) & (y_clean <= y_lim[1])
        x_plot = x_clean[mask_y]
        y_plot = y_clean[mask_y]
        
        ax.plot(x_plot, y_plot, 'b-', linewidth=2, label=nom)
        
        # Tracer les asymptotes
        if 'verticales' in asymptotes:
            for av in asymptotes['verticales']:
                if -6 <= av <= 6:  # Seulement si dans la fenêtre d'affichage
                    ax.axvline(x=av, color='r', linestyle='--', alpha=0.7, 
                              label=f'Asymptote verticale x={av:.2f}')
        
        if 'horizontale_+∞' in asymptotes and 'horizontale_-∞' in asymptotes:
            if asymptotes['horizontale_+∞'] == asymptotes['horizontale_-∞']:
                y_h = asymptotes['horizontale_+∞']
                if y_lim[0] <= y_h <= y_lim[1]:
                    ax.axhline(y=y_h, color='g', linestyle='--', alpha=0.7,
                              label=f'Asymptote horizontale y={y_h:.2f}')
        
        # Configuration du graphique
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(nom, fontweight='bold')
        ax.legend()
        ax.set_ylim(y_lim)
        
        if i == 0:
            ax.set_xlim(-3, 3)
        else:
            ax.set_xlim(-5, 5)
    
    # Supprimer le quatrième subplot vide
    fig.delaxes(axes[3])
    
    plt.tight_layout()
    plt.savefig('analyse_fonctions.png', dpi=300, bbox_inches='tight')
    plt.close()  # Fermer la figure pour libérer la mémoire
    
    print(f"\n{'='*60}")
    print("ANALYSE TERMINÉE")
    print("Le graphique a été sauvegardé sous 'analyse_fonctions.png'")
    print(f"{'='*60}")

if __name__ == "__main__":
    analyser_et_tracer()