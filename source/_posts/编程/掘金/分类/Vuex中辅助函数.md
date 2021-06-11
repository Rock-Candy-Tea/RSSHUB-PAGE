
---
title: 'Vuex中辅助函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3208'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:38:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=3208'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一般获取vuex中的值或者调用方法：</p>
<p>this.$store.commit(“xxx”),</p>
<p>this.$store.dispatch(“xxx”),</p>
<p>this.$store.state.xxx,</p>
<p>因为这样显得十分累赘，所以此时就推荐用辅助函数来替代。</p>
<p>举例：</p>
<pre><code class="copyable">import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios"

Vue.use(Vuex)

export default new Vuex.Store(&#123; 
    state: &#123;    
        uname:""  
    &#125;,  
    mutations: &#123;     
        setUname(state,uname)&#123;      
            state.uname=uname;    &#125;  
        &#125;,  
    actions: &#123; 
        //专门负责发送异步ajax请求，从服务器端获取数据    
        login(context,user)&#123; 
            //context代表整个vuex对象     
             (async function()&#123;        
                var result=await axios.get( "/users/signin",&#123;params:user&#125;);        
                context.commit("setUname",result.data.uname);      
        &#125;)()    
    &#125;  
&#125;,  
    modules: &#123;  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-0">mapState</h3>
<p>当一个组件需要获取多个状态时候，将这些状态都声明为计算属性会有些重复和冗余。为了解决这个问题，我们可以使用 mapState 辅助函数帮助我们生成计算属性，让你少按几次键：</p>
<pre><code class="copyable"><template>
    <h1 v-else>Welcome &#123;&#123;uname&#125;&#125;</h1>
</template>
<script>
import &#123;mapState&#125; from "vuex"
export default &#123;  
    computed:&#123;    
    // 使用对象展开运算符将此对象混入到外部对象中    
    ...mapState(["uname"])  
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">mapMutation</h3>
<pre><code class="copyable"><template>
    <button @click="logout">注销</button>
</template><script>
import &#123;mapMutations&#125; from "vuex"    
export default &#123;    
    methods:&#123;        
        logout()&#123;            
            this.setUname("");        
        &#125;,       
         //和其他方法同级        
        ...mapMutations(["setUname"])       
        //setUname(uname)&#123; this.$store.commit("setName",uanme) 
    &#125;    
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">mapActions</h3>
<pre><code class="copyable"><template>
    <div class="home"> 
       用户名:<input v-model="uname"><br>        
       密码:<input type="password" v-model="upwd"><br>
       <button @click="myLogin">登录</button>
      </div>
</template>
<script>
import &#123;mapActions&#125; from "vuex"
export default &#123;  
    name: 'home',
    data()&#123;    
        return &#123;      
            uname:"dingding",      
            upwd:"123456"    
        &#125;  
    &#125;, 
    methods:&#123;    
        myLogin()&#123;      
            this.login(&#123;//给user        
                uname:this.uname,        
                upwd:this.upwd      
            &#125;);        
        &#125;,    
      //去vuex的actions中取出名为login的函数放到此地         
      ...mapActions([ "login"])      //"logout","registor"                 /**原方法: 
        *  login(user)&#123;      
        *  this.$store.dispatch("login",user)     
        * &#125;,     
        */  &#125;&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            