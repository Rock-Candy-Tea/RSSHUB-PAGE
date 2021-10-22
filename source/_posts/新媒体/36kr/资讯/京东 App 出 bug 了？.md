
---
title: '京东 App 出 bug 了？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20211022/v2_bea39dea9b5946e28abf9adeb2e1bd84_img_000'
author: 36kr
comments: false
date: Fri, 22 Oct 2021 07:00:09 GMT
thumbnail: 'https://img.36krcdn.com/20211022/v2_bea39dea9b5946e28abf9adeb2e1bd84_img_000'
---

<div>   
<p>昨天文章里我说了一个关于电商产品「默认地址」设计的案例，但后来想了下，其实我说得还不够严谨和完整，所以今天再补充一下。</p> 
<p>后台有读者留言关于<a class="project-link" data-id="27570" data-name="京东" data-logo="https://img.36krcdn.com/20210806/v2_40d01763039949f194e3818a1b4fa75d_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/27570" target="_blank">京东</a>和淘宝 App 在默认地址设计上的差异，为此我也实际体验了一下，确实发现了一些差别。</p> 
<p>这种差别，在一部分读者看来是 bug，可我恰恰认为这是一种更好的产品设计。</p> 
<p>先看一个具体场景，这是淘宝 App 的购物车和结算页。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20211022/v2_bea39dea9b5946e28abf9adeb2e1bd84_img_000" referrerpolicy="no-referrer"></p> 
<p>在这个场景里，我设置了两个收货地址，一个是默认地址 X、一个是普通地址 A。</p> 
<p>接下来，我按如下步骤进行操作：</p> 
<p>1、购物车 - 结算页 - 选择地址 A - 返回购物车；</p> 
<p>2、接着 1 的操作，再进入结算页，此时地址从之前选择的 A 变成了默认地址 X；</p> 
<p>有读者说，这个很合理啊，既然设置了默认地址，就应该每次下单时都自动选择。要不然，设置默认地址干嘛？</p> 
<p>确实，从逻辑上这是没问题的。</p> 
<p>好，接下来我们再看一下京东 App 在同样场景下的设计方案。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20211022/v2_9ceed3d4bd084ad1be10528030877fa4_img_000" referrerpolicy="no-referrer"></p> 
<p>在京东 App 上的场景条件以及操作步骤和之前一样：</p> 
<p>1、购物车 - 结算页 - 选择地址 A - 返回购物车；</p> 
<p>2、接着 1 的操作，再进入结算页，不同的是，此时地址依然是 A，没有自动变成默认地址 X；</p> 
<p>针对这个区别，有读者说淘宝的设计更好，因为这发挥了「默认地址」功能的作用。</p> 
<p>还有读者说，是不是京东 App 出 bug 了？为啥设置了默认地址，但每次下单前没有选择呢？</p> 
<p>其实，不是京东 App 出了 bug，而是他们的设计更符合用户真实使用场景。</p> 
<p>我接着试了下，当我从京东 App 的结算页下单并进入收银台支付以后，此时如果再回到购物车进行<a class="project-link" data-id="63893" data-name="下一件" data-logo="https://img.36krcdn.com/20210807/v2_66dd9c1455304106a1077d1296bb22c6_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/63893" target="_blank">下一件</a>商品的结算，地址就自动变回了默认地址。</p> 
<p>也就是说，京东默认地址的生效时机是在用户下单完成并进入下一轮商品结算开始前。</p> 
<p>用过电商 App 的都知道，当你下单成功后，原本购物车的商品是会清空的。因此，你也就进入了下一个购物流程，此时默认地址就可以发挥作用了。</p> 
<p>而淘宝的默认地址生效时机是在用户每次进入结算页的时候，不管有没有下单、不管有没有修改地址，都会自动帮用户改回默认地址。</p> 
<p>在我看来，这种设计不是一个很好的解决方案。</p> 
<p>说一个具体的场景。</p> 
<p>你有两个收货地址，一个是作为默认地址的公司地址，一个是作为普通收货地址的家庭住址。</p> 
<p>比如今天周五，你今天下单买的东西预计明天就能到货，所以你大概率会选择家庭住址作为收货地址。</p> 
<p>在你没有下单之前，在购物车和结算页之间切换有可能是为了增加下单商品，也有可能是忘了勾选需要结算的商品。</p> 
<p>如果每次退回购物车再回到结算页就自动改成默认地址，那你很可能将原本应该在家收货的商品改成在公司收货，这就十分尴尬。</p> 
<p>再看京东的方案。</p> 
<p>用户在购物车和结算页之间来回切换时并不会自动更改用户已选择的地址，而是以用户上次的操作记录为准。</p> 
<p>这么做有一个好处，每一步操作都衔接用户上一次的操作结果。</p> 
<p>此外，京东在默认地址设置一栏写了一句文案：「每次下单会默认推荐使用该地址」。</p> 
<p>这说明，并不是强制更改使用默认地址，而是根据地址选择情况来判断是否使用。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20211022/v2_0206d094987f43a8a071300b528fa063_img_000" referrerpolicy="no-referrer"></p> 
<p>而淘宝在同样的地方没有做其他提示。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20211022/v2_9ecc354e460640ea8bc55d315132eea6_img_000" referrerpolicy="no-referrer"></p> 
<p>从我自己的实际体验来看，我认为京东的方案更好，而淘宝出错的概率会更高。</p> 
<p>不过对于这个场景的方案设计，可能不同人有不同的理解。</p> 
<p>毕竟，我上面提到的场景出现频率不算太高，而且两个产品的用户也都用了这么久了，大家已经形成了自己的用户习惯。</p> 
<p>在我看来，产品设计中的逻辑正确要优先服从场景正确，让用户高效完成用户任务，才是产品设计的主要目的。</p> 
<p>所以，我不认为京东这个设计是一个 bug，相反，这是一个更好的设计。</p> 
<p>对于这两种设计，没有对错，只有习惯。</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MjM5NTIzMTY2MQ==&mid=2650420901&idx=1&sn=10044e83dafcdca936a78182f400fbd8&chksm=bef534678982bd719dc1596599722015326e4e707e525a177ab13322c636f26d832984408728&scene=27#wechat_redirect">“唐韧”（ID：RyanTang007）</a>，作者：唐韧，36氪经授权发布。</p>  
</div>
            