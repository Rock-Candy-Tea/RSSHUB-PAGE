
---
title: '哪些你不得不知道的vue开发技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8524'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 01:12:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=8524'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h1 data-id="heading-0">代理和https里面的地址配置</h1>
<p>在vue开发过程中，我们会遇到一个问题就是跨域，那么我们都知道跨域就是在配置文件中配置就好了，但有的新手就懵逼了，到底用哪个地址。这里首先要明白配置文件里面的跨域配置只是针对开发阶段，也就是说开发的时候调用同事的ip地址或者是测试服地址。通常我们在封装接口请求的https里面配置的地址一个是开发环境一个是生产环境的，这里的开发环境的地址比较特殊，通常都是根据跨域配置中匹配规则来的，如通常的/api等写法。</p>
<h1 data-id="heading-1">自动载入目录下的自定义指令和过滤器</h1>
<p>我们知道vue2开发的时候会有一个叫过滤器、一个叫自定义指令的东西，那么这两个东西都是可以局部和全部配置的，如果全局配置的话如果是多个文件如何自动加载呢，首先我们看过滤器：
过滤器的话通常我们都会定义在一个文件里面通过export default导出，然后再main.js中导入即可。</p>
<pre><code class="copyable">// 注册全局过滤器
import filters from './filters'
Object.keys(filters).forEach(key => &#123;
Vue.filter(key, filters[key])
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自定义指令呢就比过滤器稍微多一点，比如通常会一个指令单独为一个文件来定义，那么指令目录下就会有很多文件，通过件文件读取然后加入到vue中</p>
<pre><code class="copyable">// 自动获取directives目录下的自定义指令并注册全局
Vue.use((Vue)=>&#123;
  ((requireContext) => &#123;
    const arr = requireContext.keys().map(requireContext);
    (arr || []).forEach((directive) => &#123;
      directive = directive.__esModule && directive.default ? directive.default : directive
      Object.keys(directive).forEach((key) => &#123;
        Vue.directive(key, directive[key])
      &#125;)
    &#125;)
  &#125;)(require.context('./directives', false, /^\.\/.*\.js$/))
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">异步产生错误</h1>
<p>我们在开发vue或者是其他框架项目时，惠遇到一种情况就是明明接口成功获取到数据了，但是还是报错说找不到某个值，那么这个时候获取你就该看看是不是因为异步的原因导致的，通常我们的静态页面是会先渲染，然后接口可能还没获取到，页面已经渲染完了，这样就会导致这个问题，如何解决呢，很简单做个判断就行：</p>
<pre><code class="copyable"><template>
  <div>&#123;&#123;info.params && info.params.name&#125;&#125;</div>
</template>

<script>
export default &#123;
  data()&#123;
    return&#123;
      info:&#123;&#125;
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">表格操作列弹窗修改值</h1>
<p>在做后台管理系统时，通常表格操作列里面会有修改某一行的数据，通过弹窗形式修改，如果我们将这一样的数据直接赋值给一个变量，那么你在修改后会发现表格里面的数据也跟着修改了，这个时候你就是需要将这一行数据进行拷贝过后赋值给变量才会不受影响。</p>
<pre><code class="copyable">editItem(row)&#123;
  // this.detailInfo = row
  this.detailInfo = JSON.parse(JSON.stringify(row))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">表格操作列删除</h1>
<p>在表格的操作列上如果我们想要删除一行数据那么我们可以这样做：</p>
<pre><code class="copyable">handleDel(index,rows)&#123;
  rows.splice(index, 1)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">方便的深拷贝</h1>
<p>JSON.parse(JSON.stringify(row))</p>
<h1 data-id="heading-6">样式中修改ui组件的值</h1>
<p>我们知道在vue的项目中如果给样式加上了scoped后是不能直接修改ui组件的样式，要么全局修改要么就需要在修改样式之前加上/deep/关键字来修改才会有效果</p>
<pre><code class="copyable"><style lang="less" scoped>
.price &#123;
  /deep/.edit-dialog &#123;
    .el-select &#123;
      width: 100%;
    &#125;
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">修改数组中某一项的值</h1>
<pre><code class="copyable">this.$set(this.tableData[index],'isEdit',false)
this.$set(this.table,'thead[3].label','优惠券金额')
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">策略模式解决很多ifelse判断</h1>
<pre><code class="copyable">this[key]
this['couponList'+couponType]
this['save'+this.activeName]()
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">字符串快速转为数值</h1>
<pre><code class="copyable">this.editInfo.item * 1
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">图片下载</h1>
<pre><code class="copyable">downloadQrcode(el,name)&#123;
    var oQrcode = document.querySelectorAll('.'+el+' img');
    var url = oQrcode[0].src
    var a = document.createElement('a')
    var event = new MouseEvent('click')
    // 下载图名字
    a.download = name+'.png';
    a.href = url;
    a.setAttribute("target", "__blank");
    // if(el != 'oilall' || el != 'exall')&#123;
    //     this.downloadIamge(url,name);
    // &#125;else&#123;
    //     // 合成函数，执行下载
    //     a.dispatchEvent(event)
    // &#125;
    a.dispatchEvent(event)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">合并数据去掉重复项</h1>
<pre><code class="copyable">reduceArr(arr,disArr)&#123;
  // 数组去重，去掉已经选中的
  var result = arr.filter(function(coupon) &#123;
    return disArr.every(function(item) &#123;
      return item.id !== coupon.id
    &#125;)
  &#125;)
  return disArr.concat(result)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">element UI 自定义传参的解决方法</h2>
<p>这里的handleSelect默认绑定的参数是选中的那条数据。如果一个页面有好几个相同的组件，要想知道选的是哪个？</p>
<pre><code class="copyable"><el-autocomplete
    v-model="state4"
    :fetch-suggestions="querySearchAsync"
    placeholder="请输入内容"
    @select="handleSelect"
></el-autocomplete>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方案：</p>
<pre><code class="copyable"><el-autocomplete
    v-model="state4"
    :fetch-suggestions="querySearchAsync"
    placeholder="请输入内容"
    @select="($event,index)"
></el-autocomplete>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">element-UI 框架 el-input 触发不了 @key.enter事件</h2>
<pre><code class="copyable"><el-input v-model="form.loginName" 
placeholder="账号" 
@keyup.enter="doLogin">
</el-input>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方案：使用@key.center.native</p>
<pre><code class="copyable"><el-input v-model="form.loginName"
placeholder="账号" 
@keyup.enter.native="doLogin">
</el-input>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            