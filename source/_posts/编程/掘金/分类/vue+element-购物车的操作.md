
---
title: 'vue+element-购物车的操作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e50f3d4a838d4432af1cf13afbef7d17~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:47:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e50f3d4a838d4432af1cf13afbef7d17~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0"><a href="https://juejin.cn/post/6943479614065311775"></a>第一种：效果预览</h5>
<p><img alt="图片预览" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e50f3d4a838d4432af1cf13afbef7d17~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
<img alt="预览" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f9623db26124f5d8b7ea73fe77b73d4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
<img alt="移除功能" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fee0031b3fbd4b50bd863e6c171c420e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-1"><a href="https://juejin.cn/post/6943479614065311775"></a>思路分析</h5>
<p>这个其实不麻烦，首先我们被选中的table是属于多选的，也就是说element是提供了一个被选中的行的数组函数的，那么这样我们可以拿到用户是选择了哪些行的，这是第一步，第二步是我们怎么保证每一页选择了以后别的页被选中的选项还在，这个我之前的博客是更新了，这里不说怎么实现的了，也是一个字段就可以了，第三步就是我们将用户选择的数据新加到购物车的那个table里面，第四步就是怎么在上面操作例如删除的时候，对应的原来用户选择的页消除了，这个是麻烦的一个地方。</p>
<h5 data-id="heading-2"><a href="https://juejin.cn/post/6943479614065311775"></a>代码实现</h5>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-comment">/**
       * <span class="hljs-doctag">@add</span>_goods 加入结账栏   这个就是加入结账栏的按钮
       */</span>
      <span class="hljs-function"><span class="hljs-title">add_goods</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">if</span>(that.tableData_check_out_transit.length === <span class="hljs-number">0</span>)&#123;
          that.hintInfo(<span class="hljs-string">'warning'</span>,<span class="hljs-string">'您还未选择任何账单！'</span>);
        &#125;<span class="hljs-keyword">else</span>&#123;
          that.hintInfo(<span class="hljs-string">'success'</span>,<span class="hljs-string">'添加成功！'</span>);
          <span class="hljs-comment">//tableData_check_out_transit  这个就是主页上的表格，这个数据是用户选择的数  据，触发的函数是@selection-change ，</span>
          <span class="hljs-comment">//tableData_check_out是购物车里面的table </span>
          that.tableData_check_out = that.tableData_check_out_transit;
          <span class="hljs-comment">//to_check_out 进行移除操作的时候可以直接进行计数</span>
          that.to_check_out = that.tableData_check_out.length;
        &#125;
      &#125;,
      <span class="hljs-comment">/**
       * <span class="hljs-doctag">@open</span>_goods 打开结账栏  用于计算需要支付的账单
       */</span>
       <span class="hljs-function"><span class="hljs-title">open_goods</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
        that.calculate();
      &#125;,
      <span class="hljs-comment">/**
       * <span class="hljs-doctag">@calculate </span>计算总金额
       */</span>
       <span class="hljs-function"><span class="hljs-title">calculate</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
        that.separate_id = [];
        that.tableData_check_out.map(<span class="hljs-function">(<span class="hljs-params">res</span>)=></span>&#123;
          count = count + res.charge_amount;
          that.separate_id.push(res.id); <span class="hljs-comment">//将用户选择的当前行的id拿到，作为参数</span>
          <span class="hljs-built_in">console</span>.info(res.charge_amount);
        &#125;);
        that.count_settle = count;
        <span class="hljs-built_in">console</span>.info(that.count_settle);
        <span class="hljs-built_in">console</span>.info(that.separate_id);
      &#125;,
       <span class="hljs-comment">/**
       * <span class="hljs-doctag">@removeRow </span>待结账栏移除操作   购物车h5 中table的移除的操作
       */</span>
      <span class="hljs-function"><span class="hljs-title">removeRow</span>(<span class="hljs-params">index, row, TableData</span>)</span>&#123;
        <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
        TableData.splice(index, <span class="hljs-number">1</span>);
        <span class="hljs-keyword">if</span>(that.to_check_out > <span class="hljs-number">0</span>)&#123;
           that.to_check_out -- ;
           that.hintInfo(<span class="hljs-string">'success'</span>, <span class="hljs-string">'移除成功！'</span>);
           that.calculate();<span class="hljs-comment">//将数据重新计算  这里是计算结账的价格</span>
           that.toggleSelection(row); <span class="hljs-comment">//移除需要的移除的元素  </span>
        &#125;<span class="hljs-keyword">else</span>&#123;
           that.hintInfo(<span class="hljs-string">'warning'</span>, <span class="hljs-string">'没有数据！'</span>);
        &#125;
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--结账栏H5--></span>
    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span>
    <span class="hljs-attr">title</span>=<span class="hljs-string">"待结账栏"</span>
    <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"dialog_settle"</span>
    <span class="hljs-attr">width</span>=<span class="hljs-string">"40%"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-table</span>
      <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData_check_out"</span>
      <span class="hljs-attr">height</span>=<span class="hljs-string">"400px"</span>
      <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>
      <span class="hljs-attr">:cell-style</span>=<span class="hljs-string">"&#123;textAlign:'center'&#125;"</span>
      <span class="hljs-attr">:header-cell-style</span>=<span class="hljs-string">"&#123;background:'#303A41',color:'#fff',fontSize:'x-small',textAlign:'center'&#125;"</span>
      <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"account_id"</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"index"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"序号"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"account_id.id"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"主账id"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"code_income_type_id.name"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"入账代码"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"biz_date"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"营业日期"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"charge_amount"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"消费金额"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"pay_status"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"支付状态"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"scope.row.pay_status === 0"</span>></span>未支付<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"scope.row.pay_status === 1"</span>></span>已支付<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"scope.row.pay_status === 2"</span>></span>异常<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-else</span>></span>无数据<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">fixed</span>=<span class="hljs-string">"right"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"操作"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span>
            @<span class="hljs-attr">click.native.prevent</span>=<span class="hljs-string">"removeRow(scope.$index, scope.row,tableData_check_out)"</span>
            <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
            <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span>></span>
            移除
          <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>PS:这里将H5也贴出来了，目的是为了更好的理解函数作用。</p>
</blockquote>
<h5 data-id="heading-3"><a href="https://juejin.cn/post/6943479614065311775"></a>第二种：效果预览</h5>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d34ae1ff402046d9987b4d86843889aa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd6356de472044148056924c1c9cab22~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4"><a href="https://juejin.cn/post/6943479614065311775"></a>思路分析</h5>
<p>这种购物车和上面的不一样，相对来说会难一点，难点在怎么在点击相同的物品的时候直接新加一个，而不是新加一列，那么我们需要做的就是，用户点击了某一列的时候，我们拿到这个数据的id，和上面的表格进行比对，判断是不是已经存在了，如果存在，那么直接进行数量加一，不新加一列。反之加一列</p>
<h5 data-id="heading-5"><a href="https://juejin.cn/post/6943479614065311775"></a>代码分析</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//merchandise_name 函数是点击切换option的时候触发的函数</span>
<span class="hljs-function"><span class="hljs-title">merchandise_name</span>(<span class="hljs-params">value</span>)</span>&#123;
          <span class="hljs-keyword">let</span> that =<span class="hljs-built_in">this</span>;
          <span class="hljs-built_in">console</span>.log(value);
          that.$axios(&#123;
            <span class="hljs-attr">url</span>:that.api.api_9530_9503+<span class="hljs-string">"/v1/stock/product_product/get/"</span>+value,
            <span class="hljs-attr">method</span>: <span class="hljs-string">"get"</span>,
          &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
              <span class="hljs-keyword">if</span>(res.data.message===<span class="hljs-string">"success"</span>)&#123;
                <span class="hljs-built_in">console</span>.log(res);
                res.data.data.account_number=<span class="hljs-number">1</span>;
                res.data.data.money=res.data.data.list_price;<span class="hljs-comment">//计算价格</span>
                <span class="hljs-keyword">let</span> ayy = &#123;&#125;;
                <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> that.account_arr)&#123;
                    ayy[i.id] = i.name;
                &#125;
                <span class="hljs-keyword">if</span>(value <span class="hljs-keyword">in</span> ayy)&#123;
                  <span class="hljs-comment">//nothing...</span>
                &#125;
                <span class="hljs-keyword">else</span>&#123;
                  that.account_arr.push(res.data.data);
                  that.merchandise_list_data = that.account_arr;
                &#125;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"step"</span>);
              &#125;
            &#125;)
            .catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
                <span class="hljs-built_in">console</span>.error(error)
            &#125;);
          <span class="hljs-comment">//处理的是如果存在的话直接进行数字加一</span>
          <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i =<span class="hljs-number">0</span>;i< that.account_arr.length;i++)&#123;
             <span class="hljs-keyword">if</span>(value === that.account_arr[i].id)&#123;
               <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"重复"</span>);
               <span class="hljs-built_in">console</span>.log(that.account_arr[i].account_number);
               that.account_arr[i].account_number+=<span class="hljs-number">1</span>;
             &#125;<span class="hljs-keyword">else</span> &#123;
               <span class="hljs-comment">//nothing....</span>
             &#125;
          &#125;
          that.merchandise_list_data= that.account_arr;
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>PS:这个逻辑的处理我不是我写的，拿来做参考是可以的，但是不难理解的，希望可以记录一下。<br>
喜欢的可以关注一下，鄙人的文采不好，所以写的能看懂就行，不明白的可以直接说问题，我看到会回复的。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            