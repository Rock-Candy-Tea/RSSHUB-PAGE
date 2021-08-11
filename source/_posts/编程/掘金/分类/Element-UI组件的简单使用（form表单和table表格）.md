
---
title: 'Element-UI组件的简单使用（form表单和table表格）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2951'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 00:59:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=2951'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1、表单</h3>
<p>表单常用来用户注册登录等提交数据</p>
<h5 data-id="heading-1">1.1表单绑定数据</h5>
<pre><code class="copyable"><el-form :model="form" :rules="rules">
    <el-form-item label="用户名">
    <el-input v-model="form.username"></el-input>
    </el-form-item>
</el-form>
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>data中的数据form应该这样写</p>
<pre><code class="copyable">form:&#123;
    username:'',
    password:'',
    &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">1.2给表单添加验证规则 注意prop是写在<code>el-form-item</code>中</h5>
<pre><code class="copyable"><el-form  :rules="rules">
    <el-form-item label="用户名" prop="name">  //name是rules里面设定的规则
    <el-input v-model="form.username"></el-input>
    </el-form-item>
</el-form>
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>data中的数据这样写</p>
<pre><code class="copyable"> rules: &#123;
        name: [
          &#123; required: true, message: '请输入用户名', trigger: 'blur' &#125;,
        ],
      &#125;,
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">1.3通常在表单提交之前会进行表单的预校验</h5>
<pre><code class="copyable"><el-form :model="form" :rules="rules" ref="form">
    <el-form-item label="用户名">
    <el-input v-model="form.username"></el-input>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="submitForm">立即创建</el-button>
    </el-form-item>
</el-form>
<script>
  export default &#123;
      methods:&#123;
           submitForm()&#123;
               this.$refs.form.validate(valid=>&#123;
               if(valid) this.$message.success('提交成功')
               &#125;)
              &#125;
            &#125;  
      &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">1.4表单的重置</h5>
<pre><code class="copyable"><el-form :model="form" :rules="rules" ref="form">
    <el-form-item label="用户名">
    <el-input v-model="form.username"></el-input>
    </el-form-item>
    <el-form-item>
        <el-button type="primary" @click="resetForm">立即创建</el-button>
    </el-form-item>
</el-form>
<script>
  export default &#123;
      methods:&#123;
           resetForm() &#123;
                this.$refs.form.resetFields();
              &#125;
            &#125;  
      &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">1.5自定义表单验证规则</h5>
<pre><code class="copyable"><el-form  :rules="rules" ref="ruleForm" label-width="100px" >
  <el-form-item label="密码" prop="pass">
    <el-input ></el-input>
  </el-form-item>
  <el-form-item label="年龄" prop="age">
    <el-input ></el-input>
  </el-form-item>
</el-form>
<script>
  export default &#123;
    data() &#123;
      var checkAge = (rule, value, callback) => &#123;
        if (!value) &#123;
          return callback(new Error('年龄不能为空'));
        &#125;
        setTimeout(() => &#123;
          if (!Number.isInteger(value)) &#123;
            callback(new Error('请输入数字值'));
          &#125; else &#123;
            if (value < 18) &#123;
              callback(new Error('必须年满18岁'));
            &#125; else &#123;
              callback();
            &#125;
          &#125;
        &#125;, 1000);
      &#125;;
      var validatePass = (rule, value, callback) => &#123;
        if (value === '') &#123;
          callback(new Error('请输入密码'));
        &#125; else &#123;
          if (this.ruleForm.checkPass !== '') &#123;
            this.$refs.ruleForm.validateField('checkPass');
          &#125;
          callback();
        &#125;
      &#125;;
      var validatePass2 = (rule, value, callback) => &#123;
        if (value === '') &#123;
          callback(new Error('请再次输入密码'));
        &#125; else if (value !== this.ruleForm.pass) &#123;
          callback(new Error('两次输入密码不一致!'));
        &#125; else &#123;
          callback();
        &#125;
      &#125;;
      return &#123;
        rules: &#123;
          pass: [
            &#123; validator: validatePass, trigger: 'blur' &#125;
          ],
          checkPass: [
            &#123; validator: validatePass2, trigger: 'blur' &#125;
          ],
          age: [
            &#123; validator: checkAge, trigger: 'blur' &#125;
          ]
        &#125;
      &#125;;
    &#125;,
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">1.6动态增减表单</h5>
<p>1.7表单样式 嵌套在 el-form-item 中的 el-form-item 标签宽度默认为零，不会继承 el-form 的 label-width。如果需要可以为其单独设置 label-width 属性。</p>
<h3 data-id="heading-7">2、Table表格</h3>
<p>表格分为2部分，el-table,el-table-column</p>
<h5 data-id="heading-8">2.1基本使用</h5>
<pre><code class="copyable"> <template>
    <el-table :data="tableData">  //data绑定数据
      <el-table-column prop="date" label="日期"></el-table-column>   //label是表格的第一行，即表头
      <el-table-column prop="name" label="姓名"></el-table-column>  //prop对应展示数据,
    </el-table>
  </template>
  <script>
    export default &#123;
      data() &#123;
        return &#123;
          tableData: [&#123;
            date: '2016-05-02',
            name: '王小虎',
          &#125;, &#123;
            date: '2016-05-04',
            name: '王小虎',
          &#125;]
        &#125;
      &#125;
    &#125;
  </script>
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">2.2样式</h5>
<p>带斑马纹：只需在<code>el-table</code>加个stripe</p>
<p>带边框：只需在<code>el-table</code>加个border</p>
<p>宽度：每个<code>el-table-column</code>,</p>
<h5 data-id="heading-10">2.3 table展开列和作用域插槽的使用</h5>
<pre><code class="copyable"><template>
  <el-table :data="tableData">
    <el-table-column type="expand">
      <template slot-scope="props">
            <span>&#123;&#123; props.row.name &#125;&#125;</span>
      </template>
    </el-table-column>
    <el-table-column label="商品 ID" prop="id"></el-table-column>
  </el-table>
</template>
<script>
  export default &#123;
    data() &#123;
      return &#123;
        tableData: [&#123;
          id: '12987122',
          name: '好滋好味鸡蛋仔',
        &#125;]
      &#125;
    &#125;
  &#125;
</script>
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其它的组件在后续文章...</p></div>  
</div>
            