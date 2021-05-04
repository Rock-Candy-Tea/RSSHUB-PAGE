
---
title: 'vue遇到拖拽动态生成组件怎么办？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa4311ac26b3414a8db77f6125770cf9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 04 May 2021 02:26:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa4311ac26b3414a8db77f6125770cf9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";@keyframes spin&#123;0%&#123;transform:rotate(0)&#125;to&#123;transform:rotate(1turn)&#125;&#125;.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#36ace1;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;color:#36ace1&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"";display:block;position:absolute;left:0;top:0;bottom:0;margin:auto;background-image:url(data:image/png;base64,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);animation:spin 2s linear 1s infinite&#125;.markdown-body h1&#123;position:relative;font-size:30px;padding:12px 38px;margin:30px 0&#125;.markdown-body h1:before&#123;width:30px;height:30px;background-size:30px 30px&#125;.markdown-body h2&#123;position:relative;font-size:24px;padding:12px 36px;margin:28px 0&#125;.markdown-body h2:before&#123;width:28px;height:28px;background-size:28px 28px&#125;.markdown-body h3&#123;position:relative;font-size:18px;padding:4px 32px;margin:26px 0&#125;.markdown-body h3:before&#123;width:24px;height:24px;background-size:24px 24px&#125;.markdown-body h4&#123;position:relative;padding:4px 28px;font-size:16px;margin:22px 0&#125;.markdown-body h4:before&#123;width:20px;height:20px;background-size:20px 20px&#125;.markdown-body h5&#123;position:relative;padding:4px 26px;font-size:15px;margin:20px 0&#125;.markdown-body h5:before&#123;width:18px;height:18px;background-size:18px 18px&#125;.markdown-body h6&#123;position:relative;padding:4px 22px;font-size:14px;margin:16px 0&#125;.markdown-body h6:before&#123;width:16px;height:16px;background-size:16px 16px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#36ace1,#dff0fe,#36ace1);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:50px;height:24px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAEgElEQVRIS72Va0xbZRjH/z2FcimbchEQFDYRCIRAAWFQ2MaCXBwmUxYDLGGEcRFkH9wmk04zG0Bo2dwNIisERANqhjqdEmhd4nRbuwpsXDYWLLoRgeG4Chu9QHvMOQ0dpTAKH3y/tDnv8/5/z/Oc//scBv6nxdgoJ14gVYPEuITHdTdHY12gRIH0T0KljlqwthqUFHGtzAEsxqwLtPvkdc+FeeI3BgMeAMEhdOqR1mM7xswBrgmKE8pfIUhtm7fbZsft/i7wc98MtrUFxmbU6ByYgFwxjtFp5Q+WpF1mCy9wajXoqqD4E91saOf603e+5B7t99xTkyZJEiKJAl2DE9Xio1HvrBS8IuhVwVUP503swdJ9QWAw1izaoDs6pQT/655BMS9yy3KYiUoM/7adu7NmtnQfx5zWm8Q8Ui3gyGcddyU8rv/STRNQouDGP5/mhTubX4dpPv3DMzh1qS9LwuPWr+i63WVyn5QYj/4d/i4bqmbpoQ+auvBlQYghX6PE4wTSOzV5EUYlb5Q4MDqLk9/3cMRF27spDSNQamUnWZ4ebNB+OKNCyYVeFCZ5wZ5tiePN/UiP2YoQL0cUX+iFt4sNUiLdcaVvHJLecQiWnKVE8s5LvxAXRWeYgHLre0hecgAN0sxr0XBZgbJUP6OiLnaM4ivZCBrzOWBZEIY9rY5E8pl2nM0KMzzLq5aPiXmRzgbQm2VyR8KGGK/ICAFB6IusbvsDwhRf+n/jtSHc/nsGgjR9V6/1TyLa1wGU+FtnO1CbHQTHTSzIFJOYJ1jwcGLTccMTcyhp7oW4KFJ/SV4/IScrc55kQj07WNuOn94Lpw8kCm/Qv3W5HLjbWxsyfuNUO1TzWjAJBloKt2FBS+Jz6ShiA12NupBdLWugQcmn28lPMkONNql3U5cTSD9Lq+qEUqPFt++G0aKL687wDAqb+pAU7IKCuK2493AOPQ9UCNpib6T1tkg+RZ9KKJcNn8sJc1vac8o16jklLWLuOiDqwvHUIKPw7vtTON+iCDKkl/Cx9FeSYET5um1mHt6jN0Dz9ftwYjORudNjTdaBmi7kxvvA1d6Gjs0X/Q5Sp3tMEMSHre9HnDEZAPFCWUNVdliGJVPvqEP1Hbh4yPj9LadSY6fu6gPsCX+B3mq7NYLv2od8fj4aoViMNQGFijos/XVMTXGavgUisQIle71hwVx9KFEutLVjw8GORTuxoEbeJS7iPrmQyy/sIj2hQpqYHO7ZGs95nnZS4y8K8Pfqrb58UZ+IlKqbqNgfQm8da+pC9xjLqo8foFkau2qaCeXSyvzXfA9SDrp1bxJ/DU/jSJKXEWdBR2J/9U0UpwXTFZ/+8S76h/71FvO4A8sTeuqQThDKalOiPLN3BbhiYlaNsm964elkCztrC4xMqeDqYIus2JdB3cbS5l4MTag44qJt9GxbF4gKThRKY59lW13+KCUQ1pZMEwHKviKx4pFSqXzxCn/X9Gr2NO+zw+cTiTbxmUyCqH3GlsWg2kRNhOnHmhlrFkIvHTZt1borWvMCmRnwH4usn58STiycAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body del&#123;color:#36ace1&#125;.markdown-body code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#282c34;color:#4ec9b0;padding:.24em .46em;margin:0 4px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;font-size:12px;border-radius:10px;padding:15px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#4ec9b0;background:#282c34&#125;.markdown-body a&#123;text-decoration:none;color:#409eff;border-bottom:1px solid #409eff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#007bff;border-bottom:1px solid #007bff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;position:relative;padding:8px 26px;background-color:rgba(54,172,225,.75);margin:16px 0;border-left:4px solid #409eff;border-radius:5px&#125;.markdown-body blockquote:before&#123;content:"❝";top:10px;left:8px;color:#409eff;font-size:20px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:20px;position:absolute;right:8px;bottom:0;color:#409eff;opacity:.7&#125;.markdown-body blockquote>p&#123;color:#fff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">产品需求</h2>
<p>开完产品需求会议，遇到了一个需求，首先页面分成两栏布局，左侧展示数据组件，支持拖拽排序，点击按钮清除组件。右侧支持将组件的缩略图拖拽至左侧生成一个新的组件。</p>
<h2 data-id="heading-1">思路</h2>
<p>对于动态生成组件来说每一次都要是生成全新的一个组件，那么就可以把 <strong>组件放进函数当中 return</strong>。在JSX中调用函数，每次调用函数都会返回一个全新的组件。<strong>这对React来说非常简单</strong>，但是对于Vue来说，直接将组件返回是不可能的。尽管这个 <strong>return</strong> 写法不适合Vue，但是我们不可否认，思路是非常正确的，所以我们应该考虑一个别的写法。至于动态的生成组件，我们必须以数据来驱动组件的生成。对于拖拽组件的排序，直接使用拖拽库就OK了！！</p>
<h2 data-id="heading-2">面临的问题</h2>
<ol>
<li>拖拽库的选择</li>
<li>如何生成组件</li>
<li>以数据驱动动态生成组件</li>
</ol>
<h2 data-id="heading-3">拖拽库的选择</h2>
<p>拖拽库在这里我选择的是项目中存在的一个拖拽库 <a href="https://github.com/SortableJS/Vue.Draggable" target="_blank" rel="nofollow noopener noreferrer">Vue.Draggable 点这里链接查看</a> Start 14.9K 蛮不错的。如果你们的Vue项目中没有用到这个拖拽库，你们可以自行参考本片文章的设计思路。</p>
<h2 data-id="heading-4">如何生成组件</h2>
<p>在这里我使用的是 Vue.extend() 不清楚如何使用的小伙伴请在官方文档中查看过后再来学习这篇文章 <a href="https://cn.vuejs.org/v2/api/#Vue-extend" target="_blank" rel="nofollow noopener noreferrer">Vue.extend</a> 。 接下来我们创建一个js文件，用来书写创建组件的代码。</p>
<h3 data-id="heading-5">生成组件</h3>
<pre><code class="copyable">/* generateComponents.js 文件名 */

import Vue from "vue";

// 想要动态生成的组件，先引入这个文件。
import components1 from "./components/TestCom1.vue";
import components2 from "./components/TestCom2.vue";

// 将组件的名称和组件做一个对应Map
const comMap = &#123;
  components1,
  components2,
&#125;;

// 接收生成组件需要的组件名称，和想要传递给组件的
// props, 和 事件
const ReturnNewCom = function (&#123; props, on &#125;) &#123;
  const &#123;
    comItem: &#123; name &#125;,
  &#125; = props;
  const newComponent = Vue.extend(&#123;
    render(createElement) &#123;
      // 使用传进来的组件name来决定渲染哪一个组件。
      return createElement(comMap[name], &#123;
        props,
        on,
      &#125;);
    &#125;,
  &#125;);
  return new newComponent();
&#125;;

export default ReturnNewCom;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">组件</h3>
<p>在这里我们书写两个组件，用来演示这个Demo，分别为components1.vue,components2.vue。</p>
<pre><code class="copyable">/*components1.vue*/
<template>
  <div class="widget-wrapper">
    <header class="header">&#123;&#123; comDetail.name &#125;&#125;--&#123;&#123; comDetail.id &#125;&#125;</header>
    <h1>查询条件：&#123;&#123; queryObj &#125;&#125;</h1>
    <button @click="handleDelete">清除</button>
  </div>
</template>
<script>
export default &#123;
  data() &#123;
    return &#123;
      comDetail: this.comItem,
      _queryObj: this.queryObj,
    &#125;;
  &#125;,
  props: &#123;
    comItem: &#123;
      type: Object,
      default() &#123;
        return &#123;
          id: 0,
          name: "",
        &#125;;
      &#125;,
    &#125;,
    queryObj: &#123;
      // 可以接收父组件传递的晒选条件，必须是Object
      type: Object,
      default() &#123;
        // 定义默认的查询条件。
        return &#123;
          num: 0,
        &#125;;
      &#125;,
    &#125;,
  &#125;,
  watch: &#123;
    comItem(val) &#123;
      this.comDetail = val;
      return val;
    &#125;,
    queryObj(val) &#123;
      this._queryObj = val;
      return val;
    &#125;,
  &#125;,
  created() &#123;
    console.log("data -> this.comItem", this.comItem);
  &#125;,
  methods: &#123;
    handleDelete() &#123;
      // 删除组件方法
      this.$el.remove();
      // 调用父组件的函数。修改父组件中的 leftComList 数组的数据。
      this.$emit("handleDelete", this.comDetail);
    &#125;,
  &#125;,
&#125;;
</script>
<style scoped>
.widget-wrapper &#123;
  background: #ff7b7b;
  border-radius: 12px;
  overflow: hidden;
  width: 200px;
&#125;
.header &#123;
  height: 50px;
  padding: 0 15px;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实components2.vue文件中的代码和components1.vue文件的代码类似，唯一不同的地方就是背景颜色不一样。</p>
<h2 data-id="heading-7">以数据驱动动态组件的生成</h2>
<p>接下来就得使用Vue.Draggable 这个拖拽库进行拖拽和数据的修改。
我们可以直接在App.vue文件中直接书写。</p>
<pre><code class="copyable">/* App.vue */
<template>
  <div class="dragCom">
    <h1>&#123;&#123; leftComList &#125;&#125;</h1>
    <button @click="queryObj.num++">改变查询条件</button>
    <div class="body">
      <div class="left">
        <draggable class="left" :list="leftComList" :group="'people'">
          <div
            ref="comBody"
            v-for="(&#123; name, id &#125;, index) in leftComList"
            :key="id"
            class="comCard"
          >
            <!-- 循环 leftComList 数组，利用数据来渲染组件， 
            将动态生成的数组添加到这个DOM元素当中。 -->
            &#123;&#123;
              handleAddCom(&#123;
                props: &#123; comItem: &#123; name, id &#125;, queryObj &#125;,
                index,
              &#125;)
            &#125;&#125;
          </div>
        </draggable>
      </div>
      <div class="right">
        <draggable
          class="dragArea"
          :list="rightComList"
          :group="&#123; name: 'people', pull: 'clone', put: false &#125;"
          :clone="handleCloneDog"
        >
          <div class="card" v-for="element in rightComList" :key="element.id">
            &#123;&#123; element.name &#125;&#125;
          </div>
          <!-- 右侧的 卡片 数据， rightComList 数组对象中的name就对应了generateComponents.js
          中的ComMap中的属性 -->
        </draggable>
      </div>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import CreateCom from "./generateComponents";
export default &#123;
  components: &#123;
    draggable,
  &#125;,
  data() &#123;
    return &#123;
      rightComList: [
        &#123;
          id: Math.random(),
          name: "components1",
        &#125;,
        &#123;
          id: Math.random(),
          name: "components2",
        &#125;,
      ],
      leftComList: [], // 存储驱动动态生成组件的数据。
      comMap: new Map(), // 主要的作用就是用来记录 
      // 组件有没有渲染到 class="comCard" 这个DOM中,
      // 如果渲染了就不能再往进添加子元素了。
      queryObj: &#123;
        // 主要的作用就是向子组件传递查询条件
        num: 0,
      &#125;,
    &#125;;
  &#125;,
  beforeDestroy() &#123;
    // 清除 记录 的数据
    this.comMap.clear();
  &#125;,
  methods: &#123;
    handleAddCom(&#123; index, on = &#123;&#125;, props = &#123; comItem: &#123; name: "", id: 0 &#125; &#125; &#125;) &#123;
      const &#123;
        comItem: &#123; id, name &#125;,
      &#125; = props;
      this.$nextTick(() => &#123;
        // 获取该节点的子节点的长度
        const childNodesLength = this.$refs.comBody[index].childNodes.length;
        // 获取comBody 这个DOM 数组的长度
        const comLine = this.$refs.comBody.length;
        if (!this.comMap.get(id)) &#123;
          // 如果没有渲染过组件

          // 1. 调用 CreateCom 方法 创建组件。 并传递 props 和 事件
          const com = CreateCom(&#123;
            name,
            props,
            on: &#123;
              handleDelete: this.handleDeleteCom,
              ...on,
            &#125;,
          &#125;);
          // 2. 生成组件
          com.$mount();
          if (childNodesLength === 2) &#123;
            // 如果要添加到两个组件中间。那么就将新生成的组件DOM位置进行修改放到中间。
            // 将最后的组件DOM添加到正确的位置
            this.$refs.comBody.splice(
              index,
              0,
              this.$refs.comBody[comLine - 1]
            );
          &#125;
          // 3. 将生成的组件添加到改DOM中。
          this.$refs.comBody[index].appendChild(com.$el);
          // 4. 记录该组件实现了渲染。
          this.comMap.set(id, true);
        &#125; else &#123;
          // 该位置的组件已经渲染，不需要再次渲染直接返回
          return;
        &#125;
      &#125;);
    &#125;,
    handleDeleteCom(&#123; id &#125;) &#123;
      // 传递给子组件删除的方法，根据组件的id来删除数据
      const index = this.leftComList.findIndex((item) => item.id === id);
      if (~index) &#123;
        // 如果存在这个id的组件，就删除
        this.leftComList.splice(index, 1);
      &#125;
    &#125;,
    handleCloneDog(item) &#123;
      // 给 leftComList 数组添加数据
      return &#123;
        ...item,
        id: Math.random(),
      &#125;;
    &#125;,
  &#125;,
&#125;;
</script>

<style>
.dragCom &#123;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
&#125;
.body &#123;
  width: 100%;
  height: 800px;
  display: flex;
  justify-content: space-between;
&#125;
.left &#123;
  flex: 1;
  height: 800px;
  border: 1px solid pink;
&#125;
.right &#123;
  width: 20%;
  height: 800px;
&#125;
.card &#123;
  height: 50px;
  background-color: #40cec7;
  margin: 12px 0;
  font-size: 12px;
  line-height: 50px;
  cursor: pointer;
&#125;
.comCard &#123;
  margin: 12px;
  display: inline-block;
&#125;
</style>


<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就实现了动态的组件渲染和拖拽排序。</p>
<h2 data-id="heading-8">效果</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa4311ac26b3414a8db77f6125770cf9~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-05-04 17.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">源码</h2>
<p>想要尝试的同学可以自行下载本文的代码<a href="https://github.com/liu-jin-yi/drag_generate_components" target="_blank" rel="nofollow noopener noreferrer">源码github</a></p></div>  
</div>
            