
---
title: '商品SKU功能设计与优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d473ff1539ea4c9a97e621597273d46e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 03:24:04 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d473ff1539ea4c9a97e621597273d46e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>商品SKU组合的创建与查询，是<strong>电商业务</strong>最经典的开发场景之一，也是整个电商系统的<strong>最基础</strong>的功能。因为如果缺少了它，那么在电商系统中，也许连快速准确的描述定位一件商品，这样最基本的需求，都将变得困难重重，商品的<strong>库存管理</strong>也就无处谈起。</p>
<h2 data-id="heading-1">概览</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d473ff1539ea4c9a97e621597273d46e~tplv-k3u1fbpfcp-watermark.image" alt="SKU功能设计流程" loading="lazy" referrerpolicy="no-referrer">
如图所示，整体流程可分为两部分:</p>
<ol>
<li><strong>运营端</strong>。负责创建与配置SKU，运营通过操作SKU选项，生成一个SKU列表。</li>
<li><strong>用户端</strong>。负责SKU的库存状态查询，在商品详情页，需要根据用户已选规格，去SKU列表里进行匹配查找。假如用户选择完毕，能够命中一份有库存的SKU数据，就提交一个SKU-ID给到下单流程。</li>
</ol>
<p>总结: 这是一种<strong>前端为主</strong>的实现方案，SKU的<strong>创建与查询部分</strong>都由前端完成，后端只负责SKU的<strong>存储</strong>。这也是各大电商平台上的主流实现。<br>
当然也有<strong>后端为主</strong>的方案，SKU的生成或者库存查询中，<strong>每次选项操作都可以看作是一次向后端的表单提交</strong>，并且只提交必要的操作信息，后端进行SKU的创建与查询，<strong>返回前端需要的最终结果就可以了</strong>。这种方案的优势是SKU查询的<strong>库存实时性好</strong>，但无论是运营端生成SKU列表，还是用户在详情页点击选项查询库存，都是足够<strong>高频的交互</strong>，每次的异步请求查询，出loading，都会打断使用者的当前操作。并且这种实现方式前端工作量很少，所以本文不会涉及。<br>
为了更清晰的内容讲解，笔者整理了一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFEyudong%2Fsku-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FEyudong/sku-demo" ref="nofollow noopener noreferrer">sku-demo</a>，包含了 1. 怎样在运营端进行SKU的创建；2.用户端怎样在商品详情页进行SKU的查询。这两项功能。麻雀虽小，五脏俱全，读者可以下载并把项目跑起来，对照着来阅读，会理解的更快。</p>
<p><strong>项目简介：</strong></p>
<ol>
<li>采用react-hook技术栈</li>
<li>用useContext+useReducer模拟了一个小型的<strong>全局Store</strong></li>
<li>运营配置页（src/views/CreateSKU.tsx）负责配置两份数据：一份是<strong>属性选项列表</strong>(attrList), 另一份是<strong>SKU列表</strong>（skuList),输出到用户详情页（src/views/SearchSKU_xxx.tsx）用来渲染选项UI及查询SKU信息，将这两份数据存入Store中,当做用户端与运营端的共享数据，已此来<strong>模拟前台与后台的一个完整交互</strong>。</li>
</ol>
<h2 data-id="heading-2">一、SKU创建</h2>
<p><code>npm start</code>启动项目后，会默认进入一个模拟<strong>运营端</strong>的商品配置页。如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c52348ce9e64e7d9eeef02e1a75cadc~tplv-k3u1fbpfcp-watermark.image" alt="demo-home" loading="lazy" referrerpolicy="no-referrer">
<em>tip:</em> 点击页面左上角的入口按钮可以进行运营端与用户端的切换。<br>
整体操作：就是运营通过<strong>操作左侧各种规格选项，联动生成右侧的SKU列表</strong>。</p>
<h3 data-id="heading-3">需求关键点分析：</h3>
<p>运营对规格选项的操作大致可分为两类：</p>
<ol>
<li>对属性的<strong>具体选项</strong>进行增删改<br>
会影响属性选项的个数，需要在SKU列表中合适的位置进行插入或者删除操作。</li>
<li>对<strong>属性</strong>进行增删<br>
会影响数据的层数，意味之前所有的SKU数据的选项组合都不是最新的了，需要清空，重新组合。</li>
</ol>
<p>为了降低程序设计的复杂度，采用了如下的设计：不区分操作，无论哪种操作类型，统一都走重新组合生成的逻辑。（当然如果十分在乎性能，也可以通过区分操作进行优化，类似于vue中针对不同dom操作类型所进行的domDiff效率方面的优化）。
所以就是将不同类型的规格值，通过排列组合的方式，生成右侧这样一个SKU的列表。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbd9ec72212b4da38830908693b533d3~tplv-k3u1fbpfcp-watermark.image" alt="SKU生成" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">具体实现：</h3>
<p>实质是求商品规格的SKU全排列组合。这个过程是一个典型的树形结构，需要遍历到这颗树的每一片叶子。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20b3cc7637b9430f9d602480db1cf741~tplv-k3u1fbpfcp-watermark.image" alt="tree" loading="lazy" referrerpolicy="no-referrer">
感兴趣的可以看下leetcode上<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fcombinations%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/combinations/" ref="nofollow noopener noreferrer">组合</a>这道题的解题思路，很类似。<br>
可以用递归的思路求解：<br>
代码位置：src/views/CreateSKU.tsx</p>
<pre><code class="copyable">/**
 * @description 递归版本的SKU全排列组合
 * @param attrList 属性列表
 * @param prevSkuList 上一次的sku列表数据
 * @returns 新的sku列表数据
 */
export function createSkuList(attrList:AttrList,prevSkuList:SkuList = []):SkuList&#123;
  const  skuList:SkuList = [];//收集结果
  let id = 0;//生成skuId
  // 旧的SkuList转map，方便下方的复用判断
  const prevSkuMap = skuList2Map(prevSkuList);
  
  const loop = (rowIndex:number,prevOptions:AttrSetItem[])=>&#123;
    const attrItem = attrList[rowIndex];
    if(attrItem.options.length === 0)&#123;
      loop(rowIndex +1,prevOptions)
      return
    &#125;
    for(const option of attrItem.options)&#123;
      const curOptions = prevOptions.concat(&#123;
        label:attrItem.attrLabel,
        value:option.value
      &#125;);
      if(rowIndex === attrList.length - 1)&#123;//判断如果是最后一层，那就是组合完整了，将结果收集到全局的容器里
        id ++;
        const key = curOptions.map((&#123;value&#125;)=>value).join('_'); // 将sku的选项值用'_'连接起来组成一个key
        if(prevSkuMap[key])&#123;// 如果改变前后的sku key相同，复用sku数据,避免数据覆盖
          skuList.push(&#123;
            ...prevSkuMap[key],
            id:`$&#123;id&#125;`
          &#125;)
        &#125;else&#123;
          skuList.push(&#123;
            id:`$&#123;id&#125;`,
            key,
            attrSet:curOptions,
            stock:0
          &#125;)
        &#125;
      &#125;else&#123;
        loop(rowIndex +1,curOptions)
      &#125;
    &#125;
  &#125;
  loop(0,[])
  return skuList
&#125;
/**
 * @description sku列表数据转map,方便映射查找，判断sku数据对比复用
 * @param skuList  sku列表
 * @returns skuKey做键,sku数据做值的sku查找映射
 */
function skuList2Map(skuList:SkuList)&#123;
  return skuList.reduce<&#123;[skuKey:string]:SkuInfo&#125;>((map,sku)=>&#123;
    map[sku.key] = sku;
    return map
  &#125;,&#123;&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了递归，也可以用循环来求解。但他们本质其实都是一样的，都是n^m的时间复杂度，循环只是靠迭代中的临时变量tempList，模拟了递归里栈的概念，所以与递归版本的区别就是使用系统的栈还是自己代码里的栈。</p>
<pre><code class="copyable">/**
 * @description 循环版本的SKU全排列组合
 * @param attrs 属性列表
 * @param prevSkuList 上一次的sku列表数据
 * @returns 新的sku列表数据
 */
export function createSkuList1(attrList:AttrList,prevSkuList:SkuList = []):SkuList&#123;
    let skuList:SkuList = [];
    let id = 0;//用来生成skuId

    // 旧的skuList转下map，方便下方的复用判断
    const prevSkuMap = skuList2Map(prevSkuList)

    attrList.forEach((row)=>&#123;//1. 遍历规格大类
      if(row.options.length === 0)&#123;
        return
      &#125;
      if(skuList.length === 0)&#123;// 初始化第一层
        skuList = row.options.map((option)=>&#123;
          id ++
          const attrSet = [&#123;label:row.attrLabel,value:option.value&#125;]
          return &#123;
            id:`$&#123;id&#125;`,
            key:attrSet.map((&#123;value&#125;)=>value).join('_'),
            attrSet,
            stock:0
          &#125;
        &#125;);
      &#125;else&#123;
        const tempList:SkuList = [];
        id = 0;
        skuList.forEach((skuItem)=>&#123;//2. 遍历当前已累积的规格组合
          row.options.forEach((option)=>&#123;//3. 遍历当前规格值，并将值与所有已累积的规格进行拼接
              id ++;
              const attrSet = skuItem.attrSet.concat(&#123;label:row.attrLabel,value:option.value&#125;);
              const key = attrSet.map((&#123;value&#125;)=>value).join('_');
              if(prevSkuMap[key])&#123;// 如果改变前后的sku key相同，复用sku数据,避免覆盖
                tempList.push(&#123;
                  ...prevSkuMap[key],
                  id:`$&#123;id&#125;`
                &#125;)
              &#125;else&#123;
                tempList.push(&#123;
                  id:`$&#123;id&#125;`,
                  key,
                  attrSet,
                  stock:0
                &#125;)
              &#125;
            &#125;)
        &#125;); 
        if(row.options.length > 0)&#123;
          skuList = tempList
        &#125;  
    &#125;
  &#125;)
  return skuList;
&#125;
/**
 * @description sku列表数据转map,方便映射查找，判断sku数据对比复用
 * @param skuList  sku列表
 * @returns skuKey做键,sku数据做值的sku查找映射
 */
function skuList2Map(skuList:SkuList)&#123;
  return skuList.reduce<&#123;[skuKey:string]:SkuInfo&#125;>((map,sku)=>&#123;
    map[sku.key] = sku;
    return map
  &#125;,&#123;&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的代码我就不展开讲解了。但是有一点是需要格外注意的，SKU列表里的数据，虽然每次都重新生成一遍，但之前针对已经配置过的内容数据（比如库存数量）在<strong>重新生成前后，选项组合并无改变的情况下，是需要保留的</strong>，不然这些数据就全丢失了，所以在创建时就给每条sku数据定义一个key（就是sku的所有选项值拼接而成的字符串）。例如：对于选项组合为<code>[M,红，宽松]</code>的sku，<code>M_红_宽松</code>就作为它的一个唯一key标示，重新创建时，会拿着新生成sku-key在旧的sku数据里的查找，如果找到有一样的，就<strong>复用原来的数据</strong>，这样就避免了重新生成后导致的原数据覆盖丢失。<br>
这样运营端SKU的生成部分工作就完成了，下边讲用户端SKU的查询。</p>
<h2 data-id="heading-5">二、SKU查询</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60a3112668d342c5967a2df13fc5d276~tplv-k3u1fbpfcp-watermark.image" alt="商品详情页" loading="lazy" referrerpolicy="no-referrer"><br>
这是SKU查询功能的截图，这里产品经理一般都会提一个交互需求：<strong>希望根据用户当前已选的规格值，能够预判出哪些SKU组合是缺货状态，提前将对应按钮置灰。</strong><br>
比如上方截图里，<code>[红色,M,男款]</code>缺货，在选择<code>红色</code>、<code>M</code>后，就需要提前将<code>男款</code>置灰。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e3659939fe746359a202ea9cca43755~tplv-k3u1fbpfcp-watermark.image" alt="选后俩" loading="lazy" referrerpolicy="no-referrer"><br>
反着选，先选后两行的<code>M</code>、<code>男款</code>，置灰第一行的<code>红色</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05d3e47ee4d64032ad5543349aac8cac~tplv-k3u1fbpfcp-watermark.image" alt="选中间" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先选前后两行<code>红色</code>、<code>男款</code>，置灰中间的<code>M</code>。<br>
这还是只一个SKU缺货，如果两个SKU缺货呢？<br>
比如<code>[红色，M，男款]</code>、<code>[红色，M，女款]</code>缺货，也就是<code>红色</code>的<code>M</code>号都缺货。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73dde146b2d24b3cbceea77b2b3b5627~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
在这种情况下，只选择一个<code>红色</code>，就需要判断出<code>M</code>不可选。<br>
1-2个sku缺货已经需要有上边那么多置灰的情况需要判断，那么更多的sku缺货呢，想想就头大，需要判断的情况太多了，或者根本不知道从何判断。
不过通过以上的场景推演，也能总结出一些导致问题变得复杂的原因:</p>
<ol>
<li>用户<strong>选择路径不一定完整</strong>，在用户全选完整之前，就需要做判断。</li>
<li>用户<strong>选择的先后顺序并不确定</strong>，用户可以跳着选、反着选。</li>
</ol>
<p><strong>点击任意选项，都有可能触发其他位置的选项的置灰</strong>，那么就可以想到一个统一的思路：<strong>无论当前选择了什么，都遍历全部选项，站在每个选项的角度，判断需不需要将自身置灰</strong>。</p>
<p>动手实现之前，先了解下已知条件:</p>
<ol>
<li><strong>attrList: 属性列表</strong>，用来展示选项UI，并且给每个选项自定义了一个disabled字段，用来表示按钮置灰状态。</li>
</ol>
<pre><code class="copyable">attrList = [
    &#123;
        "attrLabel": "颜色",
        "options": [
            &#123;
                "value": "红色",
                "disabled": true
            &#125;,
            &#123;
                "value": "绿色",
                "disabled": true
            &#125;,
            &#123;
                "value": "蓝色",
                "disabled": true
            &#125;
        ]
    &#125;,
   ...
]
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>skuList: 运营端生成的SKU列表</strong>。判断缺货与否的数据源，stock = 0即为缺货</li>
</ol>
<pre><code class="copyable">skuList = [
    &#123;
        "id": "1",
        "key": "红色_M_男款",
        "attrSet": [
            &#123;
                "label": "颜色",
                "value": "红色"
            &#125;,
            &#123;
                "label": "尺寸",
                "value": "M"
            &#125;,
            &#123;
                "label": "款式",
                "value": "男款"
            &#125;
        ],
        "stock": 0
    &#125;,
    ...
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上边整理的思路，写出以下代码</p>
<h3 data-id="heading-6">常规的循环匹配法</h3>
<pre><code class="copyable">/**
 * @description 属性的选项状态
 * @param attrList 属性列表
 * @param skuList sku列表数据
 */
function setAttrOptionStatus(attrList:AttrList, skuList:SkuList) &#123;
  // 1.获取已选规格集合&#123;A&#125;
  const selectedSet = attrList.reduce<&#123;[props:string]:string&#125;>((arr, item) => &#123;
      item.currentValue && (arr[item.attrLabel] = item.currentValue);
      return arr
  &#125;, &#123;&#125;)
  // 2.遍历所有待选规格
  attrList.forEach((attr) => &#123;
      attr.options.forEach((option) => &#123;
          if (option.isChecked) &#123;
              return
          &#125;
          // 3.待选项&#123;x&#125;与已选项&#123;A&#125;组成新的集合B = &#123;A,x&#125;
          const nextSelectSet = &#123;...selectedSet,[attr.attrLabel]:option.value&#125;
          const keys = Object.keys(nextSelectSet);
          /* 
            4.遍历sku列表，
              看能否找到符合以下两种条件的sku
              (1)选项匹配：找到sku对应的规格集合C,判断B与C是否具有包含关系 B <= C ? 
             （2）有货的：判断库存
              查找结果为否，则此按钮需要置灰，反之亦然。
          */
          option.disabled = skuList.findIndex((sku) => &#123;
            return keys.every((attrKey)=> sku.stock > 0 && sku.attrSet.findIndex((option)=>&#123;
              return option.value === nextSelectSet[attrKey]
            &#125;) > -1)
          &#125;) === -1;
      &#125;)
   &#125;)
   return attrList
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>获取已选规格集合&#123;A&#125;。</li>
<li>遍历所有待选规格。</li>
<li>待选项&#123;x&#125;与已选项&#123;A&#125;组成新的集合B = &#123;A,x&#125;</li>
<li>遍历sku列表，看能否找到<strong>同时符合以下两种条件</strong>的sku<br>
(1)有货的：判断库存stock,是否>0<br>
(2)规格选项匹配：找到sku对应的规格集合C,判断B与C是否具有包含关系 B <= C ?</li>
</ol>
<p>查找结果为否，则此按钮需要置灰，反之亦然。<br>
尝试分析一下复杂度。假设，有 m 种规格，每一种都有 n 个选项，
步骤 2 需遍历 n x m 次，还可接受。
但是步骤 4 需要在完整遍历SKU列表（长度n^m）过程中，再判断B\C俩集合是否具有包含关系。
却并不是一个简单的过程，所以是优化的重点。</p>
<h3 data-id="heading-7">Map穷举法</h3>
<p><strong>以空间换时间：</strong> 用户选择的路径、顺序、个数都不固定，那么组成的选项集合是难以预测的，那么是不是可以<strong>提前把用户所有可能选到的sku组合都穷举出来</strong>。这样在匹配查询时效率就会快很多了，因为这本质上是因为将遍历查询匹配的工作前置了。<br>
<strong>具体思路</strong>：就是根据穷举法的思想，提前计算好一个包含任意规格组合的Map映射。<br>
首先就是将每个sku组合的进行拆分，比如<code>[红色，M，男款]</code>就可以拆成（2^n）也就是8组子选项。这可以抽象为一个求幂集的操作。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/960466f49b8c41fcb7a0d306daf06e9d~tplv-k3u1fbpfcp-watermark.image" alt="sku拆分" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">/**
 * @description js求幂集
 * @param arr
 * @returns
 */
 function powerset(arr:string[]) &#123;
  const ps:string[][] = [[]];
  for (let i = 0; i < arr.length; i++) &#123;
      for (let j = 0, len = ps.length; j < len; j++) &#123;
          ps.push(ps[j].concat(arr[i]));
      &#125;
  &#125;
  return ps;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了这个求幂集方法就可以提前计算出这个任意规格组合的Map了</p>
<pre><code class="copyable">interface AnyOptionSkuMap&#123;
  [key:string]:SkuList
&#125;
/**
 * @description 计算一个包含任意规格组合的sku映射
 * @param skuList sku列表数据
 * @returns 
 */
function computedSkuResultMap(skuList:SkuList) &#123;
  const map:AnyOptionSkuMap = &#123;&#125;

  skuList.forEach((sku) => &#123;
      if (sku.stock <= 0) &#123;//没货的，不往结果里塞
          return
      &#125;
      const ids = sku.attrSet.map((item) => item.value)
      const keysArr = powerset(ids);

      keysArr.forEach((keyArr) => &#123;
          const key = keyArr.join('_')
          const v = map[key];

          map[key] = v ? [...v, sku] : [sku]
      &#125;)
  &#125;)
  return map
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>计算结果如下:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5011f13060bd4e1097602887a70df8f4~tplv-k3u1fbpfcp-watermark.image" alt="skuMap" loading="lazy" referrerpolicy="no-referrer"><br>
接下来实现查询主函数
src/views/SearchSKU_Map.tsx</p>
<pre><code class="copyable">/**
* @description 根据当前所选属性值，更新属性按钮的禁用状态 => map版本
* @param saleAttrs
* @param skuList
* @returns
*/
function setAttrOptionStatus(attrList:AttrList, skuMap:AnyOptionSkuMap) &#123;
  // 1.获取已选规格集合&#123;A&#125;
  const selectedSet = attrList.reduce<&#123;[props:string]:string&#125;>((arr, item) => &#123;
    item.currentValue && (arr[item.attrLabel] = item.currentValue);
    return arr
&#125;, &#123;&#125;)
    // 2.遍历所有待选规格
    attrList.forEach((attr) => &#123;
      attr.options.forEach((option) => &#123;
          if (option.isChecked) &#123;
              return
          &#125;
          // 3.待选项&#123;x&#125;与已选项&#123;A&#125;组成新的集合B = &#123;A,x&#125;
          const nextSelectSet = &#123;...selectedSet,[attr.attrLabel]:option.value&#125;
          /* 
            4.将集合B的元素值拼一个字符串的key,去提前计算好的skuMap字典里查找
              若无查找结果，则此按钮需要置灰，反之亦然。
          */
          const valueArr = attrList.map((&#123; attrLabel &#125;) => nextSelectSet[attrLabel]).filter(Boolean)
          const sku = skuMap[valueArr.join('_')]
          option.disabled = sku === undefined;
      &#125;)
   &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的1、2、3步骤与上边的第一种暴力循环法，是一致的，区别是第4步的。不再是去skuList里复杂的遍历匹配，而是<strong>简单的通过判断key（由集合B的选项值按固定的顺序拼成的一个字符串）是否在结果Map中存在</strong>即能知道对应的按钮是否需要缺货置灰。<br>
<strong>优点:</strong> <strong>查询的时间复杂度降为了O1</strong>，因为查询过程简化为了一次map查找,非常快。<br>
<strong>缺点:</strong> 一次幂集拆分就有2^n个子集。全部sku就有 n^m 乘以 2^n个键值对，最终如上图所示，拆出的键值对非常多，非常陇余。初始化较慢，<strong>计算出的map键值对非常多，造成空间浪费</strong>。</p>
<h3 data-id="heading-8">无向图（待更新）</h3>
<p>未完待续，更新预告：尝试用无向图这种数据结构来进行求解。</p></div>  
</div>
            