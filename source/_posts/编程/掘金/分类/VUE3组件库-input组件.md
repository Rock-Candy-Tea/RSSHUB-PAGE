
---
title: 'VUE3组件库-input组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36d876b98314620b3bcdf9ec4f77117~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 18:45:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36d876b98314620b3bcdf9ec4f77117~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";@keyframes spin&#123;0%&#123;transform:rotate(0)&#125;to&#123;transform:rotate(1turn)&#125;&#125;.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#36ace1;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;color:#36ace1&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"";display:block;position:absolute;left:0;top:0;bottom:0;margin:auto;background-image:url(data:image/png;base64,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);animation:spin 2s linear 1s infinite&#125;.markdown-body h1&#123;position:relative;font-size:30px;padding:12px 38px;margin:30px 0&#125;.markdown-body h1:before&#123;width:30px;height:30px;background-size:30px 30px&#125;.markdown-body h2&#123;position:relative;font-size:24px;padding:12px 36px;margin:28px 0&#125;.markdown-body h2:before&#123;width:28px;height:28px;background-size:28px 28px&#125;.markdown-body h3&#123;position:relative;font-size:18px;padding:4px 32px;margin:26px 0&#125;.markdown-body h3:before&#123;width:24px;height:24px;background-size:24px 24px&#125;.markdown-body h4&#123;position:relative;padding:4px 28px;font-size:16px;margin:22px 0&#125;.markdown-body h4:before&#123;width:20px;height:20px;background-size:20px 20px&#125;.markdown-body h5&#123;position:relative;padding:4px 26px;font-size:15px;margin:20px 0&#125;.markdown-body h5:before&#123;width:18px;height:18px;background-size:18px 18px&#125;.markdown-body h6&#123;position:relative;padding:4px 22px;font-size:14px;margin:16px 0&#125;.markdown-body h6:before&#123;width:16px;height:16px;background-size:16px 16px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#36ace1,#dff0fe,#36ace1);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:50px;height:24px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAEgElEQVRIS72Va0xbZRjH/z2FcimbchEQFDYRCIRAAWFQ2MaCXBwmUxYDLGGEcRFkH9wmk04zG0Bo2dwNIisERANqhjqdEmhd4nRbuwpsXDYWLLoRgeG4Chu9QHvMOQ0dpTAKH3y/tDnv8/5/z/Oc//scBv6nxdgoJ14gVYPEuITHdTdHY12gRIH0T0KljlqwthqUFHGtzAEsxqwLtPvkdc+FeeI3BgMeAMEhdOqR1mM7xswBrgmKE8pfIUhtm7fbZsft/i7wc98MtrUFxmbU6ByYgFwxjtFp5Q+WpF1mCy9wajXoqqD4E91saOf603e+5B7t99xTkyZJEiKJAl2DE9Xio1HvrBS8IuhVwVUP503swdJ9QWAw1izaoDs6pQT/655BMS9yy3KYiUoM/7adu7NmtnQfx5zWm8Q8Ui3gyGcddyU8rv/STRNQouDGP5/mhTubX4dpPv3DMzh1qS9LwuPWr+i63WVyn5QYj/4d/i4bqmbpoQ+auvBlQYghX6PE4wTSOzV5EUYlb5Q4MDqLk9/3cMRF27spDSNQamUnWZ4ebNB+OKNCyYVeFCZ5wZ5tiePN/UiP2YoQL0cUX+iFt4sNUiLdcaVvHJLecQiWnKVE8s5LvxAXRWeYgHLre0hecgAN0sxr0XBZgbJUP6OiLnaM4ivZCBrzOWBZEIY9rY5E8pl2nM0KMzzLq5aPiXmRzgbQm2VyR8KGGK/ICAFB6IusbvsDwhRf+n/jtSHc/nsGgjR9V6/1TyLa1wGU+FtnO1CbHQTHTSzIFJOYJ1jwcGLTccMTcyhp7oW4KFJ/SV4/IScrc55kQj07WNuOn94Lpw8kCm/Qv3W5HLjbWxsyfuNUO1TzWjAJBloKt2FBS+Jz6ShiA12NupBdLWugQcmn28lPMkONNql3U5cTSD9Lq+qEUqPFt++G0aKL687wDAqb+pAU7IKCuK2493AOPQ9UCNpib6T1tkg+RZ9KKJcNn8sJc1vac8o16jklLWLuOiDqwvHUIKPw7vtTON+iCDKkl/Cx9FeSYET5um1mHt6jN0Dz9ftwYjORudNjTdaBmi7kxvvA1d6Gjs0X/Q5Sp3tMEMSHre9HnDEZAPFCWUNVdliGJVPvqEP1Hbh4yPj9LadSY6fu6gPsCX+B3mq7NYLv2od8fj4aoViMNQGFijos/XVMTXGavgUisQIle71hwVx9KFEutLVjw8GORTuxoEbeJS7iPrmQyy/sIj2hQpqYHO7ZGs95nnZS4y8K8Pfqrb58UZ+IlKqbqNgfQm8da+pC9xjLqo8foFkau2qaCeXSyvzXfA9SDrp1bxJ/DU/jSJKXEWdBR2J/9U0UpwXTFZ/+8S76h/71FvO4A8sTeuqQThDKalOiPLN3BbhiYlaNsm964elkCztrC4xMqeDqYIus2JdB3cbS5l4MTag44qJt9GxbF4gKThRKY59lW13+KCUQ1pZMEwHKviKx4pFSqXzxCn/X9Gr2NO+zw+cTiTbxmUyCqH3GlsWg2kRNhOnHmhlrFkIvHTZt1borWvMCmRnwH4usn58STiycAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body del&#123;color:#36ace1&#125;.markdown-body code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#282c34;color:#4ec9b0;padding:.24em .46em;margin:0 4px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;font-size:12px;border-radius:10px;padding:15px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#4ec9b0;background:#282c34&#125;.markdown-body a&#123;text-decoration:none;color:#409eff;border-bottom:1px solid #409eff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#007bff;border-bottom:1px solid #007bff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;position:relative;padding:8px 26px;background-color:rgba(54,172,225,.75);margin:16px 0;border-left:4px solid #409eff;border-radius:5px&#125;.markdown-body blockquote:before&#123;content:"❝";top:10px;left:8px;color:#409eff;font-size:20px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:20px;position:absolute;right:8px;bottom:0;color:#409eff;opacity:.7&#125;.markdown-body blockquote>p&#123;color:#fff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">VUE3组件库-input组件</h3>
<p>大家好，今天一起来学习vue3实现input组件，希望对你有帮助</p>
<ul>
<li>
<p>目录预览</p>
<ul>
<li>基本使用</li>
<li>朴素模式</li>
<li>文本域模式</li>
</ul>
</li>
<li>
<p>基本使用</p>
<ul>
<li>
<p>效果</p>
</li>
<li>
<p>失焦状态下</p>
</li>
</ul>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36d876b98314620b3bcdf9ec4f77117~tplv-k3u1fbpfcp-watermark.image" alt="image-20210824101158054.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">-   聚焦状态下
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81ec5351584c4a9584b2de984da67796~tplv-k3u1fbpfcp-watermark.image" alt="image-20210824101215497.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">-   新建Input.vue文件用来存放input代码

    -   div样式上加个定位，以防label跑出盒子
    -   给input框加上对应样式 并用v-model绑定值

    ```
    <template>
      <div style="position: relative"> 
        <input
          class="simple-input"
          type="text"
          v-model="value"/>
          <label class="simple-input--label">&#123;&#123; placeholder &#125;&#125;</label>
        </div>
        </template>
    ```

-   在App.vue文件中引入

    -   v-model绑定子组件的值

    ```
    <template>
      <simpleinput placeholder="请输入文本" v-model="values" />
    </template>
    <script setup>
    import simpleinput from "./components/Input.vue";
    import &#123; ref &#125; from "vue";
    const values = ref("");
    </script>
    ```

-   获取属性值

    -   在setup语法糖中，引入defineProps接收父级传进来的props

        -   接收placeholder，modelValue

        -   **注意**

            -   vue3中v-model传进来的值为modelValue

            ```
            import &#123; defineProps, defineEmits, ref &#125; from "vue";
            const props = defineProps(&#123;
              placeholder: String,
              modelValue: String,
            &#125;);
            ```

-   子组件属性与父级属性值同步

    -   在input框上定义@input方法，只要有输入就会触发

    -   引入defineEmits 并在@input方法内修改App.vue里的values

        ```
        const emits = defineEmits(["update:modelValue"]);
        let handleinput = () => &#123;
          emits("update:modelValue", value.value);
        &#125;;
        ```

-   input框聚焦和失焦状态

    -   @focus 聚焦 将底部线变为蓝色 label文字变为蓝色并向上移加上动画效果
    -   @blur 失焦 将状态复原

-   Css样式 较为简单 可自行编写
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>朴素模式</p>
<ul>
<li>
<p>效果预览</p>
</li>
<li>
<p>失焦状态</p>
</li>
</ul>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/879f3701c18141ca998f7f47396a0fd5~tplv-k3u1fbpfcp-watermark.image" alt="image-20210824101450957.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">-   聚焦状态
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4867bf95fd84d10b335339d625c1978~tplv-k3u1fbpfcp-watermark.image" alt="image-20210824101525812.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">-   朴素模式传入一个line属性

    ```
      <simpleinput placeholder="请输入文本" line v-model="values" />
    ```

-   根据line的布尔值去判断底部边框是否展示
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>文本域模式</p>
<ul>
<li>
<p>效果预览</p>
</li>
<li>
<p>失焦状态</p>
</li>
</ul>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5a0e60ee6d34434b7989d81c25c41ac~tplv-k3u1fbpfcp-watermark.image" alt="image-20210824102045468.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">-   聚焦状态
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3f1c93e2c5e457a936882bb1d63b4a1~tplv-k3u1fbpfcp-watermark.image" alt="image-20210824102117927.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">-   文本域传入一个textarea属性

    ```
    <simpleinput placeholder="请输入文本" textarea v-model="values" />
    ```

-   在Input.vue里接收textarea属性 并用v-if进行判断 如果textarea存在则input框改为textarea

    ```
     <input
          v-if="!textarea"
          class="simple-input"
          :class="[
            show ? 'simple-input--focus' : '',
            line ? 'simple-input--line' : '',
          ]"
          type="text"
          v-model="value"
          @input="handleinput"
          @focus="handleFocus"
          @blur="handleBlur"
        />
    ​
        <textarea
          v-if="textarea"
          name=""
          id=""
          class="simple-input"
          :class="[
            textarea ? 'simple-textarea' : '',
            show ? 'simple-input--focus' : '',
          ]"
          rows="8"
          @input="handleinput"
          @focus="handleFocus"
          @blur="handleBlur"
        ></textarea>
    ```

-   文本框默认可伸缩 加上resize:none 可关闭伸缩
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>自定义指令 v-focus 自动聚焦</p>
<ul>
<li>
<p>vue2写法 全局注册</p>
<pre><code class="copyable">Vue.directive('focus', &#123;
  // 当被绑定的元素插入到 DOM 中时……
  inserted: function (el) &#123;
    // 聚焦元素
    el.focus()
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>vue3写法</p>
<ul>
<li>inserted 替换成了mounted</li>
<li>之后可在组件中使用v-focus指令</li>
</ul>
<pre><code class="copyable">const app = createApp(App)
app.directive('focus', &#123;
    mounted(el) &#123;
        el.focus()
    &#125;
&#125;)
app.mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>总结</p>
<ul>
<li>今日input组件完成</li>
<li>下一篇我们继续讲解Form表单中的组件</li>
</ul>
</li>
</ul></div>  
</div>
            