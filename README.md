# EPITA computer architecture courses

- S1
  - [examinations](https://github.com/BUYMERCIER/computer-architecture-courses/tree/master/S1/examinations)
  - [lectures](https://github.com/BUYMERCIER/computer-architecture-courses/tree/master/S1/lectures)
  - [tutorials](https://github.com/BUYMERCIER/computer-architecture-courses/tree/master/S1/tutorials)
- S2
  - [examinations](https://github.com/BUYMERCIER/computer-architecture-courses/tree/master/S2/examinations)
  - [lectures](https://github.com/BUYMERCIER/computer-architecture-courses/tree/master/S2/lectures)
  - [tutorials](https://github.com/BUYMERCIER/computer-architecture-courses/tree/master/S2/tutorials)
- S3
  - [examinations](https://github.com/BUYMERCIER/computer-architecture-courses/tree/master/S3/examinations)
  - [lectures](https://github.com/BUYMERCIER/computer-architecture-courses/tree/master/S3/lectures)
  - [tutorials](https://github.com/BUYMERCIER/computer-architecture-courses/tree/master/S3/tutorials)

# EPITA Mathematics full course (S1 - S2)
- [pdf file](http://buymercier.free.fr/mathcourse.pdf)
- Examinations
  - S1
  - [S2](http://buymercier.free.fr/epita/finals_math/2016.pdf)


# Seminar 

## Basic Definitions

	Alphabet: finite set of letters

	Word: a finite orderred sequence of letters

	Language: a set of words

## Notations and vocabulary

	Σ : alphabet
	a, b, c ,d : letters
	u, v, w : words
	L : language
	|u| : the length of the word u
	|u|a : number of occurences of the letter "a" in u
	ε : the empty word
	|ε| = 0
	Σ* : the set of all words on Σ

## Concatenation 

	Let u and v be words. `u . v` is the concatenation of u and v.

## Advanced Definitions

	u is a prefix of v if there exists ```w . v = u . w```.
	u is a suffix of v if there exists ```w . v = w . u```.
	u is an infix of v if there exists ```w . x . v = w . u . x```.

	We have two words u and v (u = u0, u1, ..., un):
	if u0 < v0 then u < v
	if u0 > v0 then u > v
	if u0 = v0 then we process u1 and v1 and so on...

	We have two languages L1 and L2:
	L1 . L2 = {u . v | u ϵ L1 and v ϵ L2}

	|L| = the number of words in L. :warning: It can be infinity

	L.L = L²

## Properties

	{ε} . L = L (obvious)

	{ε} ≠ ∅ because {ε} has one word of length 0

	∅ . L = ∅

	a.b ≠ b.a
	{a}.{b} ≠ {b}.{a}

## Kleene Star

	L* = ∪Lⁱ (i ϵ N)
	Σ* = ∪Σⁱ (Σⁱ being the set of words of size i)

	ε is contained in L*
	L° = ε

	∅* = {ε} (admitted)
	∅° is not defined

	




 
