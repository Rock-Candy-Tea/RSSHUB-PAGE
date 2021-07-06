
---
title: 'Vue3全家桶升级指南一composition API'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8042'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 23:16:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=8042'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1、setup()</h4>
<p>vue3中的composition API中最重要的就是setup方法了，相当于组件的入口，所有的composition API都必须放到setup()中的使用。</p>
<p><strong>setup是在组件实例初始化之前执行的(beforeCreated之前)，是整个组件的入口函数，这个时候数据和方法还没有进行挂载，因此在setup中this并不会执行当前组件实例，也不能通过this获取组件中的数据和方法了。</strong></p>
<p><strong>在模板中使用到的变量和方法必须在setup中return出来，才能使用。</strong></p>
<pre><code class="copyable">export default &#123;
    setup()&#123;
        let name="张三"
        return &#123;name&#125;//必须在这里return，模板中才能使用过
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>setup中的参数</strong>
上面已经说过，因为setup是在beforeCreate之前执行的，所以setup中的this并不会指向当前组件实例，this的值为undefined，那么我们怎么和父子组件通信呢（之前可以通过this.$emit触发）？这时就需要用到setup的参数了。</p>
<p><strong>setup有两个参数，第一个是props，父组件传递给当前组件的prop都在这个参数对象中，第二个参数是上下文context，里面包含后attrs,emit,slots，这几个参数的用法就和vue2中的大同小异了，这里不做过多赘述。</strong></p>
<h4 data-id="heading-1">2、ref用来定义基础类型的响应式数据</h4>
<p>在setup中直接定义的变量不是响应式的，如果需要定义基础类型的响应式变量，需要使用ref来定义</p>
<pre><code class="copyable">import &#123;ref&#125; from "vue"
export default &#123;
    setup()&#123;
        let name = '张三';
        setTimeout(() => &#123;
            name = '李四';
            console.log(name);//这里的改变了，但是视图并不会更新
        &#125;, 2000);
        return &#123; name &#125;;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import &#123;ref&#125; from "vue"
export default &#123;
    let name = ref('张三');
        setTimeout(() => &#123;
            name.value = '李四';
            console.log(name.value); //李四
        &#125;, 2000);
        return &#123; name &#125;;
&#125;   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需要注意的是，通过ref定义的变量，在js中使用的时候需要通过.value来获取或者设置值，但是在模板中使用的时候不需要加.value，vue内部已经帮我们处理了。</strong></p>
<h4 data-id="heading-2">通过ref获取dom元素或者组件实例</h4>
<p>在vue2中要获取dom元素或者组件实例，直接在dom元素或者组件上添加ref="refName"，然后在js中通过this.$refs.refName就可以获取了。在vue3中，使用方式略有不同。</p>
<blockquote>
<ol>
<li>直接在dom元素或者组件上添加ref="refName"</li>
<li>在setup中定义ref，初始值为null，let refName=ref(null)，注意变量的名字一定要和dom或者组件上的ref名字保持一致。</li>
<li>在js中通过refName.value获取dom元素或者组件实例</li>
<li>注意，需要在setup总return使用到的ref变量</li>
</ol>
</blockquote>
<pre><code class="copyable"><template>
  <div ref="name">张三</div>
  <button @click="change">add</button>
  <hr />
</template>

<script>
import &#123; ref &#125; from 'vue';
export default &#123;
    setup() &#123;
        let name = ref(null);
        const change = () => &#123;
            console.log(name.value);
            name.value.innerText = '李四';
        &#125;;
        return &#123; name, change &#125;;
    &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">3、reactive用来定义引用类型的响应式数据</h4>
<pre><code class="copyable">import &#123; reactive &#125; from 'vue';
export default &#123;
    setup() &#123;
        let obj = reactive(&#123; name: '张三', age: 18 &#125;);
        setTimeout(() => &#123;
            obj.name = '李四';
            console.log(obj); //李四
        &#125;, 2000);
        return &#123; obj &#125;;
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在模板中直接通过&#123;&#123;obj.name&#125;&#125;就可以访问数据了</p>
<h4 data-id="heading-4">4、computed计算属性</h4>
<p>创建只读的计算属性</p>
<pre><code class="copyable">import &#123;ref,computed&#125; from "vue"
export default &#123;
    setup()&#123;
        let count=ref(0)
        let newCount=computed(()=>count.value+10)
        return &#123;count,newCount&#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建可读可写的计算属性，在computed中传入一个对象，通过设置get和set方法创建可读写的计算属性。</p>
<pre><code class="copyable">import &#123; ref, computed &#125; from 'vue';
export default &#123;
    setup() &#123;
        let count = ref(1);
        let newCount = computed(&#123;
            get: () => count.value + 100,
            set: val => (count.value = val - 1),
        &#125;);
        let change = () => (newCount.value += 100);//给计算属性赋值会触发set
        return &#123; count, newCount, change &#125;;
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">5、watch监听</h4>
<p><strong>监听ref类型的单个数据</strong></p>
<pre><code class="copyable">import &#123; ref, computed, watch &#125; from 'vue';
export default &#123;
    setup() &#123;
        let count = ref(1);
        let newCount = computed(&#123;
            get: () => count.value + 100,
            set: val => (count.value = val - 1),
        &#125;);
        let change = () => (newCount.value += 100);
        watch(count, (newVal, oldVal) => &#123;
            console.log(newVal, oldVal);
        &#125;);
        return &#123; count, newCount, change &#125;;
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>监听ref类型的多个值</strong></p>
<pre><code class="copyable">import &#123; ref, watch &#125; from 'vue';
export default &#123;
    setup() &#123;
        let name = ref('张三');
        let age = ref(18);

        setTimeout(() => &#123;
            name.value = '李四';
            age.value = 22;
        &#125;, 2000);

        watch([name, age], ([newName, newAge], [oldName, oldAge]) => &#123;
            console.log(newName, newAge); //李四 22
            console.log(oldName, oldAge); //张三 18
        &#125;);
        return &#123; name, age &#125;;
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>监听reactive类型的单个值</strong></p>
<pre><code class="copyable">import &#123; reactive, watch &#125; from 'vue';
export default &#123;
    setup() &#123;
        let obj = reactive(&#123; name: '张三', age: 18 &#125;);
        setTimeout(() => &#123;
            obj.name = '李四';
        &#125;, 2000);

        watch(
            () => obj.name,
            (newVal, oldVal) => &#123;
                console.log(newVal, oldVal); //李四 张三
            &#125;
        );
        return &#123; obj &#125;;
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>监听reactive类型的多个值</strong></p>
<pre><code class="copyable">import &#123; reactive, watch &#125; from 'vue';
export default &#123;
    setup() &#123;
        let obj = reactive(&#123; name: '张三', age: 18 &#125;);
        setTimeout(() => &#123;
            obj.name = '李四';
            obj.age = 22;
        &#125;, 2000);

        watch(
            [() => obj.name, () => obj.age],
            ([newName, newAge], [oldName, oldAge]) => &#123;
                console.log(newName, newAge); //李四 22
                console.log(oldName, oldAge); //张三 18
            &#125;
        );
        return &#123; obj &#125;;
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>watch添加配置项</strong>
在vue2中watch如果需要添加配置就需要传入一个对象，来配置immediate和deep，在vue3中的watch同样可以在第三个参数里添加配置</p>
<pre><code class="copyable">import &#123; ref, watch &#125; from 'vue';
export default &#123;
    setup() &#123;
        let name = ref('张三');
        let age = ref(18);

        setTimeout(() => &#123;
            name.value = '李四';
            age.value = 22;
        &#125;, 2000);

        watch(
            [name, age],
            ([newName, newAge], [oldName, oldAge]) => &#123;
                console.log(newName, newAge);
                console.log(oldName, oldAge);
            &#125;,
            &#123;
                immediate: true,
                deep: true,
            &#125;
        );
        return &#123; name, age &#125;;
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">6、watchEffect监听</h4>
<pre><code class="copyable">import &#123; ref, watch, watchEffect &#125; from 'vue';
export default &#123;
    setup() &#123;
        let name = ref('张三');
        let age = ref(18);

        setTimeout(() => &#123;
            name.value = '李四';
            age.value = 22;
        &#125;, 2000);

        watchEffect(() => &#123;
            console.log(name.value);
            console.log(age.value);
        &#125;);
        return &#123; name, age &#125;;
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>关闭监听</strong></p>
<p>创建监听的时候可以用一个变量来接收watch或者watchEffect函数的返回值，然后在需要停止监听的地方调用这个匿名函数stop()，就可以关闭了</p>
<pre><code class="copyable">import &#123; ref, watch, watchEffect &#125; from 'vue';
export default &#123;
    setup() &#123;
        let name = ref('张三');
        let age = ref(18);

        setTimeout(() => &#123;
            name.value = '李四';
            age.value = 22;
        &#125;, 2000);
        setTimeout(() => &#123;
            stop();//在这里关闭监听后，在4秒后就不会再打印信息了
            name.value = '李四2';
            age.value = 222;
        &#125;, 4000);

        let stop = watchEffect(() => &#123;
            console.log(name.value);
            console.log(age.value);
        &#125;);
        return &#123; name, age &#125;;
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>watchEffect和watch的区别</strong></p>
<blockquote>
<ol>
<li>watch默认是惰性的，只有当监听的变量发生改变时才会执行，watchEffect不是惰性的，组件初始化的时候就会执行，改变时也会执行。</li>
<li>watch需要指定要监听的变量（ref和reactive类型的变量略不同），watchEffect不需要指定，在回调中使用到的响应式变量都会监听，当这些变量改变时，回调都会执行。</li>
<li>watch可以再改变时获取到新值和旧值，watchEffect只能获取到新值。</li>
</ol>
</blockquote></div>  
</div>
            