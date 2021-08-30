
---
title: 'Nest.js 实践总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://resource5-1255303497.file.myqcloud.com/points_mall/picture/img_124476251_1630291837.png'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 03:03:31 GMT
thumbnail: 'https://resource5-1255303497.file.myqcloud.com/points_mall/picture/img_124476251_1630291837.png'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Nest.js 是一个现代的企业级 Node.js web 框架，在最近使用 Nest.js 实践一些项目的总结了一些使用心得，但也从中学到了很多东西，在这里总结下来和大家分享。</p>
<h2 data-id="heading-0">1. API 设置全局前缀</h2>
<p>为 API 设置一个全局前缀可以区分接口版本，如通常会用 <code>/api/v1</code> 作为的 API 端点的前缀。</p>
<p>为什么我们需要前缀？ 好的 API 在设计时要考虑到向后的兼容性。当增强或增加一个 API 时，我们应该确保已经线上使用到该 API的业务不受影响。"简而言之，API 前缀是为了向后兼容。</p>
<p><img src="https://resource5-1255303497.file.myqcloud.com/points_mall/picture/img_124476251_1630291837.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2. 模块划分</h2>
<p>Nest.js 是以模块化结构为基础的，服务端应用应该按功能职现被划分为几个部分，通常情况下，将你的目录结构应该按模块划分而不是按类型分成文件夹。</p>
<p>以下是按类型划分文件夹（不推荐）</p>
<p><img src="https://resource5-1255303497.file.myqcloud.com/points_mall/picture/img_1075792583_1630305274.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以下是按模块划分文件夹（推荐）</p>
<p><img src="https://resource5-1255303497.file.myqcloud.com/points_mall/picture/img_1314405626_1630305376.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于 Nest.js，模块是一个包含 <code>.module.ts</code> 文件的文件夹，其中包含一个 <code>@Module(&#123;&#125;)</code> 装饰器。但并非每个文件夹都需要有一个 <code>.module.ts</code> 文件。 例如，你可以创建一个文件夹名为 <code>utils</code> 来存储你的工具函数或 JSON 文件。</p>
<p>通过将文件组织到模块文件夹中，会变得清晰，并且可以避免很多错误。 此外，如果你不遵守此原则，Nest.js 可能会在构建过程中崩溃。</p>
<h2 data-id="heading-2">3.使用 DTOs</h2>
<p>DTO = 数据传输对象。 Dtos 就像接口，目标是传输数据并验证它，主要用于路由器/控制器。</p>
<p>你可以通过使用它们来简化 API 主体和查询验证逻辑。 例如，下面的 AuthDto 自动将用户电子邮件和密码映射到对象 DTO 以强制验证。</p>
<p><img src="https://resource5-1255303497.file.myqcloud.com/points_mall/picture/img_121184958_1630305485.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的例子是期望密码超过 5 个字符，你可以将 dtos 与 class-validator 包配对以自动抛出错误。</p>
<h2 data-id="heading-3">4. 应该使用 Data Mapper/Repository 模式，而不是 Active Record</h2>
<p>如果你正在使用 PostgreSQL 或 MySQL 等关系数据库，那么请使用 TypeOrm，它是 Typescript 最强大的 ORM 之一。</p>
<p>TypeOrm 可以使用两种模式，一种是由 ruby on rails 推广的活动记录模式，另一种是使用存储库的数据映射器模式。</p>
<p>使用 Active Record 方法，可以在模型本身内定义所有查询方法，并使用模型方法保存、删除和加载对象。
下面是使用 Active Record 模式的样子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> UserEntity();
user.name = <span class="hljs-string">"Vladimir"</span>;
user.job = <span class="hljs-string">"programmer"</span>;
<span class="hljs-keyword">await</span> user.save();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 Data Mapper 方法，你可以在称为“存储库”的单独类中定义所有查询方法，并使用存储库保存、删除和加载对象：</p>
<pre><code class="copyable">const user = this.userRepository.create();
user.name = "Vladimir";
user.job = "programmer";
await this.userRepository.save(user);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然活动记录乍一看似乎更好，但它违背了 Nest.js 提供的模块化，因为活动记录与全局实体一起工作，而数据映射器需要在使用它们之前将实体注入每个模块。</p>
<p>数据映射器可能看起来有点冗长，但它是中/大型项目的更好解决方案。 它也非常适合测试，因为它适用于依赖注入！</p>
<h2 data-id="heading-4">5. 应该使用相对路径，而不是绝对路径</h2>
<p>你可以使用绝对路径或相对路径导入 es6 模块。 但在 Nest.js 在开发中使用绝对路径，再构建应用时它会崩溃。 </p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// relative imports</span>
<span class="hljs-keyword">import</span> &#123; SecurityService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../security/security.service'</span>;
<span class="hljs-keyword">import</span> &#123; CommentService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../comment/comment.service'</span>;

<span class="hljs-comment">// absolute imports</span>
<span class="hljs-keyword">import</span> &#123; SecurityService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'src/security/security.service'</span>;
<span class="hljs-keyword">import</span> &#123; CommentService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'src/comment/comment.service'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6. 使用 Exclude 来隐藏不必要的数据</h2>
<p>使用过滤器从数据库中获取的数据是很常见的。过滤器的整个目标是删除或格式化来自数据库的数据。 这会导致很多垃圾逻辑，使代码变得更冗余。如果是需要隐藏某些字段，可以使用@Exclude() 装饰器。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Exclude &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'class-transformer'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserEntity</span> </span>&#123;
  <span class="hljs-attr">id</span>: number;
  firstName: string;
  lastName: string;
  @Exclude()
  <span class="hljs-attr">password</span>: string;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">partial: Partial<UserEntity></span>)</span> &#123;
    <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>, partial);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">7. 使用实体的 getter 方法</h2>
<p>一些通用的逻辑可以作为属性直接添加到你的实体逻辑里。 最常见的用例与密码散列和获取全名有关，这时可以使用 getter 方法，但是要注意不要过度使用，避免给实体承担大量的业务逻辑。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Exclude &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'class-transformer'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserEntity</span> </span>&#123;
  <span class="hljs-attr">id</span>: number;
  firstName: string;
  lastName: string;
  <span class="hljs-keyword">get</span> <span class="hljs-title">fullName</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">" "</span> + <span class="hljs-built_in">this</span>.lastName;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">8. 使用集中命名导出</h2>
<p>你可以从同一个文件夹中导入所有类，而不是从不同的文件中导入你的类。如有以下目录：</p>
<p><img src="https://resource5-1255303497.file.myqcloud.com/points_mall/picture/img_1768542439_1630305807.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// index.ts</span>
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'./createPost.dto'</span>;
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'./editPost.dto'</span>;
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'./editPostCategory.dto'</span>;
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'./editPostStatus.dto'</span>;

<span class="hljs-comment">// 推荐　</span>
<span class="hljs-keyword">import</span> &#123; CreatePostDto, EditPostDto &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./dto'</span>;

<span class="hljs-comment">// 不推荐</span>
<span class="hljs-keyword">import</span> &#123; CreatePostDto &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./dto/createPost.dto'</span>;
<span class="hljs-keyword">import</span> &#123; EditPostDto &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./dto/editPost.dto'</span>;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            