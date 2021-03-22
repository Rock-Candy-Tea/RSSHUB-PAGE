
---
title: """""""""'Algebraic Complexity Theory_ Where the Abstract and the Practical Meet'"""""""""
categories: 
    - 新媒体
    - Simons Foundation - 文章
author: Simons Foundation - 文章
comments: false
date: Wed, 24 Feb 2021 00:00:00 GMT
thumbnail: 'https://simonsfoundation.imgix.net/wp-content/uploads/2021/02/23113955/Zuiddam-headshot-02-23-21.jpg?auto=format&w=485&q=90'
---

<div>   
<div class="m-block-image m-block-image--right " data-behavior="image_lightbox variable_height_image" data-pid="73972" data-field="block_editor" data-field-index="0">
  <figure>
    <img src="https://simonsfoundation.imgix.net/wp-content/uploads/2021/02/23113955/Zuiddam-headshot-02-23-21.jpg?auto=format&w=485&q=90" srcset="https://simonsfoundation.imgix.net/wp-content/uploads/2021/02/23113955/Zuiddam-headshot-02-23-21.jpg?auto=format&w=485&q=90, https://simonsfoundation.imgix.net/wp-content/uploads/2021/02/23113955/Zuiddam-headshot-02-23-21.jpg?auto=format&w=485&q=90&dpr=2 2x, https://simonsfoundation.imgix.net/wp-content/uploads/2021/02/23113955/Zuiddam-headshot-02-23-21.jpg?auto=format&w=485&q=90&dpr=3 3x," alt referrerpolicy="no-referrer"><figcaption>Above: Junior Fellow Jeroen Zuiddam</figcaption>  </figure>
</div>
<div class="m-block m-block-text">
  <p>Many mathematical puzzles in everyday life, like estimating travel time or making a budget, are straightforward. The building blocks that we learn as children — addition, subtraction, multiplication, division — are sufficient for many numerical tasks we perform well into adulthood. Surprisingly, mathematicians like <a href="https://www.simonsfoundation.org/simons-society-of-fellows/">Simons Junior Fellow</a> <a href="https://www.simonsfoundation.org/people/jeroen-zuiddam/">Jeroen Zuiddam</a> use these very same tools to solve much more complex problems.</p>
<p>Zuiddam specializes in algebraic complexity theory. Complexity theory writ large explores the dynamics of complex systems — economies, climates, even the human brain — in which the interactions between the parts in those systems are hard to predict. Algebraic complexity theory uses algebraic techniques, such as factoring polynomials or squaring and cubing numbers, to solve complex computational puzzles.</p>
<p>Zuiddam earned a doctorate in mathematics and computer science from the University of Amsterdam in 2018. He then completed a postdoctoral fellowship at the Institute for Advanced Study in Princeton and is now a Simons junior fellow at New York University’s Courant Institute. His adviser at NYU is <a href="https://cims.nyu.edu/~regev/">Oded Regev</a>. After completing his Simons fellowship this summer, Zuiddam will continue as an assistant professor of mathematics at the University of Amsterdam.</p>
<p>I caught up with Zuiddam recently to discuss the appeal of algebraic complexity theory and what exactly it means to ‘compute the permanent.’ Our conversation has been edited for clarity.</p>
<p> </p>
<p><strong>First things first. What is algebraic complexity theory and how do you use it?</strong></p>
<p>Complexity theory in general is about solving computational problems algorithmically as efficiently as possible. It includes many subfields such as algebraic complexity theory. I mainly use numbers, nothing fancy — I add or subtract, multiply or divide — to build an algorithm that solves a hard computational problem. For example, I might want to quickly evaluate a complex polynomial, or rapidly determine the product of two matrices.</p>
<p>A quick vocabulary refresher: A polynomial is a math expression containing variables and coefficients, in which you can add, subtract or multiply variables. A matrix is a rectangle that contains numbers, symbols or mathematical expressions arranged in rows and columns.</p>
<p>My work is generally in the realm of pure math and does not necessarily have a direct or immediate application. That said, physicists use matrices to study how objects in an interconnected system move through space. And computing products of large matrices is a building block for many numerical algorithms. The basic tools are familiar to many people from high school algebra class.</p>
<p>These challenges are likely much more complicated than what you likely saw in your high school algebra class, though. Since the problems I study can consume lots of computer server space or require lots of bandwidth, it’s important to find an algorithm that solves these problems in as few steps as possible.</p>
<p><strong> </strong></p>
<p><strong>What drew you to this work?</strong></p>
<p>I’ve enjoyed working with computers since a young age and have always been good at math. Math can be quite abstract and conceptual, which I enjoy. On the other hand, building computer code is completely practical and focused on solving a real-world problem. Complexity theory is where abstract and practical thinking converges.</p>
<p>In some sense, complexity theory is rooted in nature. Some things can be computed, like those matrix products and polynomials, while others cannot — like the famous ‘halting problem’ for Turing machines. That problem asks: Can we predict in advance whether a computer program will ever finish running, or ‘halt’? A mathematical proof has already shown that this problem is not computable.</p>
<p>So, then: What can we compute, and how fast? These questions are based in the natural reality that many things are computational. But the beauty is that I can apply clean, abstract mathematical tools to solving them. I like this mix of nature and theory.</p>
<p>Another appeal of this work is finding connections between different problems in different domains, such as communication complexity, algebraic complexity and quantum information. What I learn in one area I try to apply in another.</p>
<p> </p>
</div>

<div class="m-block-image m-block-image--right " data-behavior="image_lightbox variable_height_image" data-pid="73972" data-field="block_editor" data-field-index="2">
  <figure>
    <img src="https://simonsfoundation.imgix.net/wp-content/uploads/2021/02/23122546/Arithemtic-circuit-02-23-21.jpg?auto=format&w=485&q=90" srcset="https://simonsfoundation.imgix.net/wp-content/uploads/2021/02/23122546/Arithemtic-circuit-02-23-21.jpg?auto=format&w=485&q=90, https://simonsfoundation.imgix.net/wp-content/uploads/2021/02/23122546/Arithemtic-circuit-02-23-21.jpg?auto=format&w=485&q=90&dpr=2 2x, https://simonsfoundation.imgix.net/wp-content/uploads/2021/02/23122546/Arithemtic-circuit-02-23-21.jpg?auto=format&w=485&q=90&dpr=3 3x," alt referrerpolicy="no-referrer"><figcaption>An example of an arithmetic circuit computing the polynomial xy + 2x + y - 1. Given a polynomial, what is the smallest arithmetic circuit that computes it? <figcredit>Credit: Jeroen Zuiddam</figcredit></figcaption>  </figure>
</div>
<div class="m-block m-block-text">
  <p><strong>What’s an example of applying knowledge from one domain to another in your own work?</strong></p>
<p>I am interested in matrix multiplication, which involves multiplying two matrices together — one with the same number of rows as the other has columns — to get a new matrix. A mathematician named Volker Strassen invented the first sophisticated algorithms for computing matrices in the 1960s; that’s when this field was born. Since then, people have developed ever-better algorithms for solving matrix multiplication problems.</p>
<p>I didn’t use these algorithms to solve yet another matrix multiplication problem, though. During the 1980s Strassen developed a framework to explain the roots of sophisticated matrix multiplication algorithms and how all the different approaches to solving matrix multiplication problems connect together. In this tour de force, he explicitly set up this framework so that others could apply his insights in different settings beyond matrix multiplication, but even so such applications hadn’t appeared even 30 years after he published this groundbreaking work.</p>
<p>During my doctoral studies I took Strassen up on his bold idea. I used Strassen’s theory on a version of a communication challenge of Claude Shannon known as the Alice and Bob problem: Two people (Alice and Bob) are texting over an unreliable internet connection that garbles a character now and then. How can we ensure that their communication is as error-free — with no glitches in the received text, for example — and as efficient as possible?</p>
<p>Communication theorists had already developed means to solve instances of this problem using their disciplinary tools. In my Ph.D. dissertation, I used the Strassen framework to show that the most efficient way to ensure error-free communication also has an alternative precise algebraic description. Here was a perfect example of using a tool from one field to solve a problem in another!</p>
<p>I am now on the lookout for other surprising ways to use Strassen’s theory, for other communication problems or computation problems.</p>
<p><strong> </strong></p>
<p><strong>That sounds very satisfying! Now let’s turn to an ongoing problem in algebraic complexity theory, known as computing the permanent. What does this involve and why is it important?</strong></p>
<p>Yes, this is one of the big open questions in the field, and many people including me have thought and are thinking about it. It’s not the kind of problem that you wake up in the morning and focus on fully, but it’s always there in the background waiting to be solved.</p>
<p>So in algebraic theory the ‘permanent’ is the opposite of the ‘determinant’ or, if you’d like, the angry brother! I say the permanent is angry because it doesn’t have an efficient algorithm, whereas its happy brother — the determinant — has an elegant solution.</p>
<p>What, then, is the determinant? It is an important polynomial defined on a matrix. Let me explain. For example, here is a simple two-by-two matrix with variables:</p>
<p style="text-align: center;"><em>A</em>11<em> A</em>12</p>
<p style="text-align: center;"><em>A</em>21<em> A</em>22</p>
<p>For this matrix, the determinant is A11 A22 − A12 A21. Let’s now increase to a three-by-three matrix, where we have these variables:</p>
<p style="text-align: center;"><em>A</em>11 <em>A</em>12 <em>A</em>13</p>
<p style="text-align: center;"><em>A</em>21 <em>A</em>22 <em>A</em>23</p>
<p style="text-align: center;"><em>A</em>31 <em>A</em>32 <em>A</em>33</p>
<p>As you can see, the determinant gets more complicated to write down: A13 A22 A31 + A12 A23 A31 + A13 A21 A32 − A11 A23 A32 − A12 A21 A33 + A11 A22 A33.</p>
<p>Luckily, we have clever algorithms that can scale up to efficiently compute the polynomials as the matrices grow larger. As long as we’re having signs in all the right places of the polynomial, all is well.</p>
<p>Alas, that’s not true when we start to add things rather than subtract. When we’re adding we’re computing the permanent. Take that same two-by-two matrix:</p>
<p style="text-align: center;"><em>A</em>11<em> A</em>12</p>
<p style="text-align: center;"><em>A</em>21<em> A</em>22</p>
<p>But now we want to compute A11 A22 + A12 A21 instead of A11 A22 − A12 A21. This seems simple, right? And yet, once you start adding things up, the established algorithms that we had been using break down. All of the algorithms that people have come up with take exponentially increasing steps. We expect that there is no efficient algorithm to compute the permanent for large matrices.</p>
<p>This challenge is connected to the famous P versus NP problem in complexity theory, which asks: Can a math problem whose solution can be verified quickly be solved just as fast? Understanding the permanent would get us closer to solving that problem too. That’s why I and many colleagues will continue to work on computing the permanent.</p>
<p><strong> </strong></p>
<p><strong>That’s fascinating — a seemingly tiny change in the mathematical landscape has such profound ripple effects. Any closing thoughts?</strong></p>
<p>Exactly right. An interesting thing about math is that little tweaks to your problem set make such a big difference. One thing I like about algebraic complexity theory is that the problems are easy to describe — it didn’t take that long to describe the permanent just now — even if the solutions are challenging! I don’t expect to solve the permanent problem myself, by any means, but I’m glad to be part of a community that is building tools to make this solution possible.</p>
</div>


    <!-- Tags Molecule -->
<!-- End Tags Molecule -->

    <!-- Related Block Molecule -->
      
<section class="m-block-info js-is-off-view" data-behavior="related_module in_view" data-align="right">
  
</section>
    <!-- End Related Block Molecule -->
    
</div>
            