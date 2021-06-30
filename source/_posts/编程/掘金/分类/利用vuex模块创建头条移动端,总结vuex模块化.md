
---
title: '利用vuex模块创建头条移动端,总结vuex模块化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5052'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 07:40:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=5052'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天学习了vuex模块化的创建,并且应用到之前用vant组件做的头条项目中去。</p>
<p>当vuex中数据越来越多，vuex会变得越来越难以维护，因此vuex的模块化可以方便我们对数据进行维护。</p>
<p>vuex的子模块存放在根模块的modules中，每个子模块都有根模块中的所有属性。子模块的state是注册在子模块局部的，mutation、action、getter是注册在全局的，如果用户为了提高子模块中数据的隐私性，可以通过配置namespaced:true开启命名空间。</p>
<h4 data-id="heading-0">组件调用vuex子模块中状态的方法：</h4>
<pre><code class="copyable">1.直接调用（带上模块的属性名路径）
<span>&#123;&#123;this.$store.子模块名称.状态名称&#125;&#125;</span>
2.利用getter
    (1)在根模块中的getters中设置:
getters:&#123;
    在组件中调用的名称:state => state.子模块名称.状态名称
&#125;
    (2)在组件中调用mapGetters
 import &#123;mapGetters&#125; from 'vuex'
    (3)在组件的计算函数中调用
 computed:&#123;
     ...mapGetters(['状态名称1','状态名称2'])
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">组件调用开启了命名空间的其他属性</h4>
<pre><code class="copyable">1.直接调用
    this.$store.dispatch/commit('属性名/方法名'，传过去的值)
2.利用辅助函数
    (1).首先引入属性
import &#123;mapMutations,mapActions&#125; from 'vuex'
    (2).调用属性(带上模块的属性名路径)
methods:&#123;
      ...mapMutations(['xxx/xxx','传回去的值'])
      ...mapActions(['xxx/xxx','传回去的值'])
&#125;
3.利用命名空间辅助函数
import &#123;createNamespacedHelpers&#125; from 'vuex'
const &#123;mapMutations&#125; = createdNamespacedHelpers('属性名')
//然后就可以正常使用属性了
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">头条tab栏利用vuex模块实现内容切换的一些知识点</h4>
<p>1.记住不论什么情况，mutations修改数据，actions执行异步任务
2.在state中存了一个对象，对象中的属性是数组值，如果修改数组中的数据，无法实现快照，因为对象属于引用型数据，我们修改的是其在堆中的地址。可以换一个思路实现快照：</p>
<pre><code class="copyable"> state: &#123;
    allList: &#123;&#125;,
  &#125;,
  mutations: &#123;
    // 更改对应的列表项
    updateList(state, &#123; currentCatagtory, list &#125;) &#123;
      state.allList = &#123; ...state.allList, [currentCatagtory]: list &#125;;
      // 这里的state.allList=&#123;...state.allList&#125;是一个浅拷贝，目的是为了实现快照
      // [key]:value --  json
    &#125;,
    actions: &#123;
    // 在这里获取所有列表，因为axios是异步函数，只能在actions中处理
    async getList(context, cataId) &#123;
      const &#123;
        data: &#123;
          data: &#123; results &#125;,
        &#125;,
      &#125; = await axios.get(
        `http://ttapi.research.itcast.cn/app/v1_1/articles?channel_id=$&#123;cataId&#125;&timestamp=$&#123;Date.now()&#125;&with_top=1`
      );
      console.log(results);
      context.commit("updateList", &#123; currentCatagtory: cataId, list: results &#125;);
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码的逻辑是，将state中的list用数组的展开运算符加上 形参[key]:value json对象，然后在actions中调用接口，获取数据，传输实参到mutations中进行数据更新，并且实现页面快照。</p></div>  
</div>
            