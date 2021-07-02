
---
title: '从概率学上看，输一把睡觉vs赢一把睡觉，哪个胜率更高一些？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic4.zhimg.com/5cb0236fb_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2021-07-02 02:20:31
thumbnail: 'https://pic4.zhimg.com/5cb0236fb_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://pic4.zhimg.com/5cb0236fb_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">王小龙，</span><span class="bio">陕师大数统院讲师</span>
<a href="https://www.zhihu.com/question/461910176/answer/1955208355" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>一个好好的数学问题为啥没人正经答题呢？</p>
<p><strong>先说结论：两种策略的赢率是一样的，但是赢率的波动性大小不同。</strong></p>
<p>假设你叫小明，玩一把游戏的获胜概率是</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p" alt referrerpolicy="no-referrer"></p>
<p>，输的概率是</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=q%3D1-p" alt referrerpolicy="no-referrer"></p>
<p>，各局游戏相互独立，有两种游戏策略：输了就睡觉和赢了就睡觉。这就带来几个问题：</p>
<ol><li><strong>什么时候能睡觉？</strong></li>
<li><strong>胜率如何？</strong></li>
<li><strong>如何稳赢？</strong></li>
</ol><p>为了分析这些问题，定义随机变量</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=X" alt referrerpolicy="no-referrer"></p>
<p>和</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=Y" alt referrerpolicy="no-referrer"></p>
<p>分别为采取"输了就睡觉"和"赢了就睡觉"策略玩游戏的总局数，那么由独立性条件可以得到概率：</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=P%5C%7BX%3Dk%5C%7D%3Dp%5E%7Bk-1%7Dq%2Ck%3D1%2C2%2C3%2C%5Ccdots" alt referrerpolicy="no-referrer"></p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=P%5C%7BY%3Dk%5C%7D%3Dq%5E%7Bk-1%7Dp%2Ck%3D1%2C2%2C3%2C%5Ccdots" alt referrerpolicy="no-referrer"></p>
<p>即前</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=k-1" alt referrerpolicy="no-referrer"></p>
<p>局连赢(输)，第</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=k" alt referrerpolicy="no-referrer"></p>
<p>局游戏第一次输(赢)的概率，这个分布称为几何分布。注意这两个分布具有对称性(把</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p" alt referrerpolicy="no-referrer"></p>
<p>和</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=q" alt referrerpolicy="no-referrer"></p>
<p>对调，问题只是换了一种陈述）。</p>
<p><strong>问题 1：什么时候能睡觉？</strong></p>
<p>计算游戏局数的期望：</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Ctext%7BE%7DX%3D1%5Ccdot+q+%2B+2%5Ccdot+pq+%2B+3%5Ccdot+p%5E2q%2B%5Ccdots%3D1%2Fq" alt referrerpolicy="no-referrer"></p>
<p>类似地，由对称性：</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Ctext%7BE%7DY%3D1%2Fp" alt referrerpolicy="no-referrer"></p>
<p>因此</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Ctext%7BE%7DX%3C%5Ctext%7BE%7DY" alt referrerpolicy="no-referrer"></p>
<p>等价于</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p%3Cq" alt referrerpolicy="no-referrer"></p>
<p>，也就是说，如果小明的胜率</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p%3C0.5" alt referrerpolicy="no-referrer"></p>
<p>，"输一把睡觉"能够更快地睡上觉。如果小明很菜，</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p%5Capprox0" alt referrerpolicy="no-referrer"></p>
<p>，采用输一把睡觉的平均游戏局数为</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Ctext%7BE%7DX%3D1%2Fq%3D1%2F%281-p%29%5Capprox1" alt referrerpolicy="no-referrer"></p>
<p>也就是基本上玩一局就能睡觉啦。反之，如果小明错误的采用"赢一把睡觉"的策略，那么他平均需要玩</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Ctext%7BE%7DY%3D1%2Fp%5Crightarrow%5Cinfty" alt referrerpolicy="no-referrer"></p>
<p>，因此对于菜鸡来说，<strong>赢一把就睡策略的潜台词是我要通宵</strong>。</p>
<p><strong>问题 2：胜率如何？</strong></p>
<p>如果采取"输了就睡觉"策略反复玩游戏</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=n" alt referrerpolicy="no-referrer"></p>
<p>天，每天一共玩</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=X_i%28i%3D1%2C2%2C%5Ccdots%2Cn%29" alt referrerpolicy="no-referrer"></p>
<p>局，其中赢</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=X_i-1" alt referrerpolicy="no-referrer"></p>
<p>局，输</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=1" alt referrerpolicy="no-referrer"></p>
<p>局，那么总共赢了</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Csum_%7Bi%3D1%7D%5En%28X_i-1%29" alt referrerpolicy="no-referrer"></p>
<p>局，输了</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=n" alt referrerpolicy="no-referrer"></p>
<p>局，赢率为：</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=r_X%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5En%28X_i-1%29%7D%7B%5Csum_%7Bi%3D1%7D%5EnX_i%7D%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5EnX_i-n%7D%7B%5Csum_%7Bi%3D1%7D%5EnX_i%7D%3D1-%5Cfrac%7Bn%7D%7B%5Csum_%7Bi%3D1%7D%5EnX_i%7D%5C%5C+%3D1-%5Cfrac%7B1%7D%7B%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5EnX_i%7D%5Capprox+1-%5Cfrac%7B1%7D%7B%5Ctext%7BE%7DX%7D%3D1-%5Cfrac%7B1%7D%7B1%2Fq%7D%3Dp" alt referrerpolicy="no-referrer"></p>
<p>其中我们用到了大数定律，大量样本的平均值趋向于期望</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5EnX_i%5Capprox+%5Ctext%7BE%7DX" alt referrerpolicy="no-referrer"></p>
<p>如果采取"赢了就睡觉"策略反复玩游戏</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=n" alt referrerpolicy="no-referrer"></p>
<p>天，每天一共玩</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=Y_i%28i%3D1%2C2%2C%5Ccdots%2Cn%29" alt referrerpolicy="no-referrer"></p>
<p>局，赢</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=1" alt referrerpolicy="no-referrer"></p>
<p>局，那么总共赢了</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=%5Csum_%7Bi%3D1%7D%5En+1%3Dn" alt referrerpolicy="no-referrer"></p>
<p>局，赢率为：</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=r_Y%3D%5Cfrac%7Bn%7D%7B%5Csum_%7Bi%3D1%7D%5EnY_i%7D%3D%5Cfrac%7B1%7D%7B%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5EnY_i%7D%5Capprox+%5Cfrac%7B1%7D%7B%5Cfrac%7B1%7D%7Bp%7D%7D%3Dp" alt referrerpolicy="no-referrer"></p>
<p>因此如果每天采取同样的策略玩游戏，长此以往，<strong>两种策略的赢率是一样的</strong>，都是</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p" alt referrerpolicy="no-referrer"></p>
<p>。这类似于如果所有人都采用一直生娃，直到生出男(女)娃停止的生育策略，那么男女比率还是 1:1。</p>
<p><strong>问题 3：如何稳赢？</strong></p>
<p>现在小明有了三种游戏策略：a.只玩一把就睡觉，b.输一把就睡觉，c.赢一把就睡觉，上面我们推导出这三种策略的胜率都是</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p" alt referrerpolicy="no-referrer"></p>
<p>。但是在现实生活中，这三种策略的实际胜率具有随机性，其波动大小并不一样。这就好比你有三种股票可以选择投资，它们的平均回报率可能都是 5%，但其波动性不同：第一种股票稳赚 5%，第二种股票可能赚 1%-%9，第三种股票可能赚 15%，也可能亏 5%，只是平均而言赚 5%。小明的人生只有一次，因此当他选择投资方式时，应该选择波动性较小或者风险较低的投资方式，甚至为较小的风险、牺牲一定回报率也是值得的。这也是为什么国债虽然利率低，但总是很抢手，因为风险极低。</p>
<p>我们可以用胜率的标准差来衡量其波动性，假设小明是高玩(</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p%3D0.9" alt referrerpolicy="no-referrer"></p>
<p>)，下图种展示了小明采取三种策略的胜率的均值和标准差，可以看到随着游戏天数增加，三种策略的平均胜率很快趋向于 0.9，但"输一把就睡"的 error bar 更窄，说明<strong>胜得更稳</strong>。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-4d4460075dc06a706c8f4d7b8efb7c81_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure><p>相反，下图表明如果小明是菜鸡(</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p%3D0.1" alt referrerpolicy="no-referrer"></p>
<p>)，采取赢一把就睡的策略，不仅能够爽玩，赢率也更稳定。如果小明的目标是提高胜率，那么采取输一把就睡策略，胜率的波动性更大，更有可能高到 0.15 以上，但也有较大可能低到 0.05 以下，如果小明兼有赌狗属性，也许会<strong>不理智地</strong>选择这种<strong>高风险策略</strong>。对于理性人来说，当平均收益(胜率)相同时，总是应该选择低风险的策略。</p>
<figure><img class="content-image" src="https://pic4.zhimg.com/v2-2055b33880f3c97c98f755913eeea8bd_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure><p><strong>总结：</strong></p>
<p>两种策略的赢率是一样的，对于高玩(</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p%3E0.5" alt referrerpolicy="no-referrer"></p>
<p>)采取赢了就睡觉策略能更快睡上觉，但赢率波动性较大，反之对于菜鸡(</p>
<p><img class="content-image" src="https://www.zhihu.com/equation?tex=p%3C0.5" alt referrerpolicy="no-referrer"></p>
<p>)，采用赢了就睡觉策略更难睡上觉。</p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/461910176">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            