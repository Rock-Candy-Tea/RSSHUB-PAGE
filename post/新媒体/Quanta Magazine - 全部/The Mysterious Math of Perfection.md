
---
title: 'The Mysterious Math of Perfection'
categories: 
    - 新媒体
    - Quanta Magazine - 全部
author: Quanta Magazine - 全部
comments: false
date: Mon, 15 Mar 2021 00:00:00 GMT
thumbnail: 'https://d2r55xnwy6nx47.cloudfront.net/uploads/2021/03/Perfect-Number_2880_Lede.jpg'
---

<div>   
<div data-reactid="197"><section class="post__title__wrapper relative" data-reactid="198"><section class="outer fill-h relative outer--content" data-reactid="199"><div class="mha container--s" data-reactid="200"></div></section></section></div><figure class="lh-0 w-100P m-0_auto d-flex align-items-center justify-content-center flex-direction-column max-width-1420 _p_last-of-type-mb-0 p-0 _19nesb1 _jrggmc _552kiq _rna4ro" data-reactid="234"><div class="w-100P d-flex justify-content-center _149bqoo _1syob6o _aylhnx _1ovb59i image--module" data-reactid="235"><div class="w-auto max-width-100P max-height-100P mr-0p5em _last-of-type-m-0 _1oyl2xe _1mmfes9 _duy6tz _aylhnx component-img" data-reactid="236"><img alt src="https://d2r55xnwy6nx47.cloudfront.net/uploads/2021/03/Perfect-Number_2880_Lede.jpg" class="w-100P max-width-100P mb-1p5rem _q2oepu _rna4ro _1oyl2xe border-none" data-reactid="237" referrerpolicy="no-referrer"><!-- react-empty: 238 --></div></div><figcaption class="d-block m-0_auto w-100P _112lb0a _192y3bk _dc69mj" data-reactid="239"><section class="p-0_3rem _k5gyt3 _rna4ro" data-reactid="240"><div class="max-width-560px w-100P m-0_auto d-flex flex-direction-column _1e0lyfy _k6y9ug _1ij7gf7 _1xqp4r2 _n5xvur _eugonq _l378w0 _149bqoo _bv6xe6 _1y275b3 _1re1wwt _pattribution-w-auto _46bwqc _pujp80 _pcaption-w-auto _1dxfdx3" data-reactid="241"><!-- react-text: 242 --><!-- /react-text --><div class="attribution theme__anchors--solid wysiwyg pangram h6 mb1 fill-h" data-reactid="243"><p><a href="https://www.behance.net/BIGMOUTH">BIG MOUTH</a> for Quanta Magazine</p>
</div></div></section></figcaption></figure><div class="acf-content scale1 mt2" data-reactid="244"><div class="post__wrapper scale0 show-dropcap" data-reactid="245"><div class="mha container--m" data-reactid="246"><div class="post__content relative flex flex-items-start flex-justify-between" data-reactid="247"><section class="outer mha js-router-anchors outer--content" data-reactid="297"><div class="flex-auto mha container--xs" data-reactid="298"><div class="post__content__section wysiwyg p theme__anchors--underline" data-reactid="299"><div class="post__content wysiwyg p theme__anchors--underline" data-reactid="300"><p>Mona Lisa’s smile. Mary Lou Retton’s Olympic vault. Mariah Carey’s musical pitch. All are considered perfect. So are the numbers 6 and 28.</p>
<p>With feats of artistry and athleticism, perfection lies in the eye of the beholder. But for numbers, perfection is mathematically defined. “Perfect numbers” are equal to the sum of their “proper” divisors (positive integers that divide a number evenly, not counting itself). For example, 6 = 3 + 2 + 1, and 28 = 14 + 7 + 4 + 2 + 1. While these mathematical curiosities are about as likely to grace the walls of the Louvre as they are to perform a twisting layout back somersault, they do offer something irresistible: a perfect mystery.</p>
<p>Euclid laid out the basics of perfect numbers over 2,000 years ago, and he knew that the first four perfect numbers were 6, 28, 496 and 8,128. Since then, many more perfect numbers have been discovered. But, curiously, they’re all even. No one has been able to find an odd perfect number, and after thousands of years of unsuccessful searching, it might be tempting to conclude that odd perfect numbers don’t exist. But mathematicians haven’t been able to prove that either. How is it that we can know so much about even perfect numbers without being able to answer the simplest question about an odd one? And how are modern mathematicians trying to resolve this ancient question?</p>
<p>Our exploration of mathematical perfection begins with divisors. We know that 6 is a divisor of 12 since <img align="center" src="https://latex.codecogs.com/png.latex?%20\frac&#123;12&#125;&#123;6&#125;" referrerpolicy="no-referrer"> = 2, and we know 25 is a divisor of 100 since <img align="center" src="https://latex.codecogs.com/png.latex?%20\frac&#123;100&#125;&#123;25&#125;" referrerpolicy="no-referrer"> = 4. As we said, we know a number is perfect when it is equal to the sum of its proper divisors — those divisors that are less than the number itself. We can also define a number as perfect when the sum of all its divisors, proper and improper, is twice the number. This works out because the only improper divisor of a number is the number itself. We see that 28 is still perfect by this definition: Its proper divisors are 1, 2, 4, 7 and 14, its improper divisor is 28, and the sum of all its divisors, 1 + 2 + 4 + 7 + 14 + 28, is 56, which is 2 × 28. Including the improper divisor in the sum is convenient for some of the algebra we’ll do with perfect numbers, as we’ll see shortly.</p>
<figure><img src="https://d2r55xnwy6nx47.cloudfront.net/uploads/2021/03/EQUATION-1_v3.svg" referrerpolicy="no-referrer"><figcaption></figcaption></figure><br>
We can factor out that 7 to reveal some hidden structure:<p></p>
<p style="text-align: center;">σ(28) = (1 + 2 + 4) + 7 × (1 + 2 + 4).</p>
<p>And with some more clever factoring with the distributive property, we can write</p>
<p style="text-align: center;">σ(28) = (1 + 2 + 4)(1 + 7).</p>
<p>This doesn’t tell us anything we didn’t already know: σ(28) = (1 + 2 + 4)(1 + 7) = 7 × 8 = 56, which confirms that 28 is perfect. But there’s something important hiding inside that multiplication:</p>
<p style="text-align: center;"><img align="center" src="https://latex.codecogs.com/png.latex?%20\begin&#123;aligned&#125;%CF%83(28)%20&=%20(1%20+%202%20+%204)%20(1%20+%207)\\&=%20(1%20+%202^1%20+%202^2)(1%20+%207^1).\end&#123;aligned&#125;" referrerpolicy="no-referrer"></p>
<p>Those expressions in parentheses look familiar: 1 + 2<sup>1</sup> + 2<sup>2</sup> = σ(2<sup>2</sup>), and 1 + 7<sup>1</sup> = σ(7). This means that we can actually write</p>
<p style="text-align: center;">σ(28) = σ(2<sup>2</sup>)σ(7).</p>
<p>To compute σ(28) = σ(2<sup>2</sup> × 7) we can actually compute σ(2<sup>2</sup>) and σ(7) and multiply them. This is a surprise, and it’s true in general: Any time you factor a number into primes like this you can use this shortcut to compute σ. For example, since 100 = 2<sup>2</sup>×5<sup>2</sup>, we can compute σ(100) like this:</p>
<p style="text-align: center;">σ(100) = σ(2<sup>2</sup>)σ(5<sup>2</sup>) = (1 + 2 + 4)(1 + 5 + 25) = 7 × 31 = 217,</p>
<p>which is a bit easier than listing all nine divisors of 100 and adding them up.</p>
<p>Why does this work? Well, the divisors of a number come from its prime factors. Consider 28 again, which is the product of 2<sup>2</sup> and 7, and think about the multiplication table below:</p>
<style>
table, .post__content table th, .post__content table td &#123;border: 1px solid black; border-collapse: collapse; padding: 0.3em; line-height: 1.1;&#125; table&#123;width: 65%; margin-left: auto; margin-right: auto; &#125; @media screen and (max-width: 544px) &#123; table &#123; width: 100%; &#125; &#125;</style>
<table>
<tbody>
<tr>
<td style="text-align: center;" width="10%"><span style="color: #ff0000;">x</span></td>
<td style="text-align: center;" width="10%">1</td>
<td style="text-align: center;" width="10%">2</td>
<td style="text-align: center;" width="10%">4</td>
</tr>
<tr>
<td style="text-align: center;" width="10%">1</td>
<td style="text-align: center;" width="10%"></td>
<td style="text-align: center;" width="10%"></td>
<td style="text-align: center;" width="10%"></td>
</tr>
<tr>
<td style="text-align: center;" width="10%">7</td>
<td style="text-align: center;" width="10%"></td>
<td style="text-align: center;" width="10%"></td>
<td style="text-align: center;" width="10%"></td>
</tr>
</tbody>
</table>
<p>Along the top are the powers of 2 that evenly divide 28, and down the side are the powers of 7 that evenly divide 28. Notice what happens when we fill out this multiplication table.</p>
<table>
<tbody>
<tr>
<td style="text-align: center;" width="10%"><span style="color: #ff0000;">x</span></td>
<td style="text-align: center;" width="10%">1</td>
<td style="text-align: center;" width="10%">2</td>
<td style="text-align: center;" width="10%">4</td>
</tr>
<tr>
<td style="text-align: center;" width="10%">1</td>
<td style="text-align: center;" width="10%"><span style="color: #0000ff;">1</span></td>
<td style="text-align: center;" width="10%"><span style="color: #0000ff;">2</span></td>
<td style="text-align: center;" width="10%"><span style="color: #0000ff;">4</span></td>
</tr>
<tr>
<td style="text-align: center;" width="10%">7</td>
<td style="text-align: center;" width="10%"><span style="color: #0000ff;">7</span></td>
<td style="text-align: center;" width="10%"><span style="color: #0000ff;">14</span></td>
<td style="text-align: center;" width="10%"><span style="color: #0000ff;">28</span></td>
</tr>
</tbody>
</table>
<p>We get all the divisors of 28. That’s because every divisor of 28 is a combination of divisors of 2<sup>2</sup> and 7, the prime powers that appear in the factorization of 28.</p>
<p>Now compare the multiplication table with the expression</p>
<p style="text-align: center;">(1 + 2 + 4)(1 + 7).</p>
<p>When we multiply this out using the distributive property, this also produces all the divisors of 28 and then adds them up:</p>
<p style="text-align: center;">(1 + 2 + 4)(1 + 7) = 1 × 1 + 2 × 1 + 4 × 1 + 7 × 1 + 7 × 2 + 7 × 4.</p>
<p>In other words, (1 + 2 + 4)(1 + 7) is exactly σ(28). But (1 + 2 + 4)(1 + 7) is also σ(2<sup>2</sup>)σ(7). So σ(2<sup>2</sup>)σ(7) = σ(28). This example demonstrates a very useful fact about σ: In the language of number theory, this function is “multiplicative.” That means that σ(<em>ab</em>) = σ(<em>a</em>)σ(<em>b</em>) whenever the numbers <em>a</em> and <em>b</em> are “relatively prime,” meaning they have no factors in common.</p>
<p>This is the special feature of σ that’s perfect for helping us study perfect numbers. Euclid used this fact 2,000 years ago to create a formula for finding perfect numbers, with help from a special kind of prime and a clever argument about products and divisors. In doing so, he took the first step toward determining what every even perfect number has to look like. Let’s see how he did it.</p>
<p>First, notice that for any power of 2 we have</p>
<p style="text-align: center;">σ(2<em><sup>k</sup></em>) = <img align="center" src="https://latex.codecogs.com/png.latex?%20\frac&#123;2^&#123;k+1&#125;-1&#125;&#123;2-1&#125;" referrerpolicy="no-referrer"> = 2<sup><em>k</em>+1</sup> – 1.</p>
<p>This is a consequence of the geometric series formula we discussed earlier. Now consider the following thought experiment: What if 2<sup><em>k</em>+1</sup> – 1 is prime?</p>
<p>Well, since σ(<em>p</em>) = 1 + <em>p</em> for any prime, we know that σ(2<sup><em>k</em>+1</sup> – 1) = 1 + 2<sup><em>k</em>+1</sup> – 1 = 2<sup><em>k</em>+1</sup>. And notice that 2<sup><em>k</em>+1</sup> is exactly twice 2<em><sup>k</sup></em>, because of the law of exponents that says 2 × 2<em><sup>k</sup></em> = 2<sup><em>k</em>+1</sup>. So we have the following two interesting relationships between the numbers 2<em><sup>k</sup></em> and 2<sup><em>k</em>+1</sup> – 1:</p>
<p style="text-align: center;">σ(2<em><sup>k</sup></em>) = 2<sup><em>k</em>+1</sup> – 1</p>
<p>and</p>
<p style="text-align: center;">σ(2<em><sup>k+1</sup></em> – 1) = 2<sup><em>k</em>+1</sup> = 2 × 2<sup><em>k</em></sup>.</p>
<p>Euclid noticed a clever way to leverage these relationships: He put the two numbers together to make the number <em>M</em> = 2<sup><em>k</em></sup> × (2<sup><em>k</em>+1</sup> – 1), and as long as (2<em><sup>k+1</sup></em> – 1) is prime, this number is perfect! To see this, we’ll compute σ(<em>M</em>) and show it is equal to 2<em>M</em>.</p>
<p>First, notice that 2<sup><em>k</em>+1</sup> – 1 is one less than an even number so it must be odd. This means 2<sup><em>k</em>+1</sup> – 1 is not divisible by 2. But 2<sup><em>k</em></sup> is only divisible by powers of 2. So 2<sup><em>k</em></sup> and 2<sup><em>k</em>+1</sup> – 1 have no common factors and are thus relatively prime. This allows us to use the multiplicative property of σ:</p>
<figure><img src="https://d2r55xnwy6nx47.cloudfront.net/uploads/2021/03/EQUATION-2_v2.svg" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<p>We already know that σ(2<em><sup>k</sup></em>) = 2<sup><em>k</em>+1</sup> – 1 and σ(2<sup><em>k</em>+1</sup> – 1) = 2<sup><em>k</em>+1</sup> = 2 × 2<em><sup>k</sup></em>, so we can find σ(<em>M</em>):</p>
<p style="text-align: center;"><img align="center" src="https://latex.codecogs.com/png.latex?%20\begin&#123;aligned&#125;\sigma(M)&=\sigma\left(2^&#123;k&#125;%20\times\left(2^&#123;k+1&#125;-1\right)\right)\\&=\sigma\left(2^&#123;k&#125;\right)%20\sigma\left(2^&#123;k+1&#125;-1\right)\\&=\left(2^&#123;k+1&#125;-1\right)\left(2%20\times%202^&#123;k&#125;\right)\\&=\left(2%20\times%202^&#123;k&#125;\right)\left(2^&#123;k+1&#125;-1\right)\\&=2\left(2^&#123;k&#125;%20\times\left(2^&#123;k+1&#125;-1\right)\right)\\&=2(M).\end&#123;aligned&#125;" referrerpolicy="no-referrer"></p>
<p>So <em>M</em> = 2<em><sup>k</sup></em> × (2<sup><em>k</em>+1</sup> – 1) is perfect, as claimed.</p>
<p>Keep in mind that this relies on the assumption that the number 2<sup><em>k</em>+1</sup> – 1 is prime. These numbers are called Mersenne primes, and you might have heard of them because of the Great Internet Mersenne Prime Search (<a href="https://www.mersenne.org/">GIMPS</a>), a collaborative online computing effort to find huge Mersenne primes. Anytime you hear about the discovery of a new largest prime number, it’s probably the result of GIMPS. And thanks to Euclid’s proof, anytime a new Mersenne prime is discovered, a new perfect number is discovered as well.</p>
<p>For example, 2<sup>5</sup> – 1 = 31 is a Mersenne prime, and so 2<sup>4</sup>(2<sup>5</sup>-1) = 16 × 31 = 496 is a perfect number. Also, 2<sup>2</sup> – 1 = 3 is a Mersenne prime, so 2<sup>1</sup>(2<sup>2</sup> – 1) = 2 × 3 = 6 is perfect. And 2<sup>3</sup> – 1 = 7 is a Mersenne prime, so 2<sup>2</sup>(2<sup>3</sup> – 1) = 4 × 7 = 28 is perfect.</p>
<p>You may have noticed that all these perfect numbers are even. This makes sense, because as long as <em>k</em> > 0, the number 2<em><sup>k</sup></em> × (2<sup><em>k</em>+1</sup> – 1) will be even. (And if <em>k</em> = 0 then 2<sup><em>k</em>+1</sup> – 1 is 1, which is not a prime.)</p>
<p>You may also have noticed that all the perfect numbers we’ve discussed so far seem to involve Mersenne primes. That’s no coincidence: 2,000 years after Euclid showed that this formula generates perfect numbers, Leonhard Euler proved that this is the only way to get even perfect numbers. But the question of what odd perfect numbers might be like (if they exist) remained open.</p>
<p>And it remains open today. Although they can’t find one, mathematicians have a lot of information about what a hypothetical odd perfect number might look like. It can’t be divisible by 105. It would have to have at least nine distinct prime factors, the second-largest of which would have to be greater than 10,000. And it would have to have a remainder of 1 when divided by 12 or a remainder of 9 when divided by 36.</p>
<p>It might seem strange to prove results about numbers that might not even exist. But every new rule narrows the search a little more. And if they’re lucky, mathematicians might just prove that odd perfect numbers have to satisfy two incompatible criteria, which would prove once and for all that no odd perfect number exists.</p>
<p>On the hunt for incompatible criteria, mathematicians have even started <a href="https://www.quantamagazine.org/mathematicians-open-a-new-front-on-an-ancient-number-problem-20200910/">looking at numbers that aren’t quite perfect</a>. A “spoof perfect number” is a number that looks perfect if you pretend one of its non-prime factors is actually prime. For example, 60, the product of 3, 4 and 5, can be considered “spoof perfect”: If you pretend that the 4 in its factorization is a prime, then the shortcuts we developed for σ give us</p>
<p style="text-align: center;">(1+3)(1+4)(1+5) = 4 × 5 × 6 = 120.</p>
<p>If σ(60) equaled 120, then 60 would be perfect. Of course, σ(60) doesn’t actually equal 120, but it looks like it if we pretend 4 is a prime. That’s what makes it a spoof.</p>
<p>These spoofs are like generalizations of perfect numbers, and so anything true about a spoof would have to be true about a perfect number as well. Understanding odd spoofs would be especially useful, since any rule discovered for odd spoofs could be added to the existing rules for odd perfect numbers, increasing the chances of finding contradictory criteria and tightening the overall search space.</p>
<figure><img src="https://d2r55xnwy6nx47.cloudfront.net/uploads/2021/03/EQUATION-3.v2.svg" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>Notice that since (<em>p</em>-1)(1 + <em>p</em> + <em>p</em><sup>2</sup> + <em>p</em><sup>3</sup> + … + <em>p<sup>n</sup></em>) = <em>p</em><sup><em>n</em>+1</sup> – 1, we can divide both sides of the equation by <em>p</em> – 1 to get</p>
<p style="text-align: center;">1 + <em>p</em> + <em>p</em><sup>2</sup> + <em>p</em><sup>3</sup> + … + <em>p<sup>n</sup></em> = <img align="center" src="https://latex.codecogs.com/png.latex?\frac&#123;p^&#123;n+1&#125;-1&#125;&#123;p-1&#125;" referrerpolicy="no-referrer">,</p>
<p>the formula for the sum of a geometric series.</p>
</div>
<p class="reveal-next" style="cursor: pointer; box-shadow: inset 0 0 0 rgba(0, 0, 0, 0), 0 1px 0 #1a1a1a; display: inline-block;">Click for Answer 4:</p>
<div class="revealable" style="color: #ffffff; visibility: hidden;">
<p>Since<em> M </em>= 2<em>N</em> and is perfect, we have σ(<em>M</em>) = σ(2<em>N</em>) = 4<em>N</em>. But since <em>N</em> is odd, <em>N</em> and 2 are relatively prime, so σ(2<em>N</em>) = σ(2)σ(<em>N</em>) = 3σ(<em>N</em>). So 4<em>N</em> = 3σ(<em>N</em>).</p>
<p>Since both sides of this equation are integers and 3 does not divide 4, 3 must divide <em>N</em>. So we can write</p>
<p style="text-align: center;">4<img align="center" src="https://latex.codecogs.com/png.latex?%20\frac&#123;N&#125;&#123;3&#125;" referrerpolicy="no-referrer"> = σ(<em>N</em>).</p>
<p>Since <img align="center" src="https://latex.codecogs.com/png.latex?%20\frac&#123;N&#125;&#123;3&#125;" referrerpolicy="no-referrer"> must be an integer, it is also a divisor of <em>N</em>. <em>N</em> is also a divisor of <em>N</em>, so we know that the sum of the divisors of N is at least the sum of these two. That is,</p>
<p style="text-align: center;">σ(<em>N</em>) ≥ <em>N</em> + <img align="center" src="https://latex.codecogs.com/png.latex?%20\frac&#123;N&#125;&#123;3&#125;" referrerpolicy="no-referrer"> = <img align="center" src="https://latex.codecogs.com/png.latex?%20\frac&#123;4&#125;&#123;3&#125;" referrerpolicy="no-referrer"><em>N</em>.</p>
<p>But we already know that σ(<em>N</em>) = <img align="center" src="https://latex.codecogs.com/png.latex?%20\frac&#123;4&#125;&#123;3&#125;" referrerpolicy="no-referrer"><em>N</em>. If <em>N</em> had any more divisors, σ(<em>N</em>) would be greater than <img align="center" src="https://latex.codecogs.com/png.latex?%20\frac&#123;4&#125;&#123;3&#125;" referrerpolicy="no-referrer"><em>N</em>, so 3 must be its only divisor. Thus <em>N</em> = 3 as claimed.</p>
<p>This is a specific application of Euler’s proof that every even perfect number is of the form <em>M</em> = 2<sup><em>k</em></sup> × (2<sup><em>k</em>+1</sup> – 1), where 2<sup><em>k</em>+1</sup> – 1 is a Mersenne prime.</p>
</div>
<p></p>
<p><em><strong>Correction:</strong> March 16, 2021</em></p><em>
</em><p><em>This article has been revised to reflect that 16 × 31 = 496, not 486. Thank you to our eagle-eyed readers for catching this typographical error, which also serves as a reminder to students to always double-check your work!</em> </p>
</div></div></section></div></div></div></div><div class="pv2" data-reactid="376"></div>  
</div>
            