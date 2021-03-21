
---
title: 使用Vue.js和MJML创建响应式电子邮件
categories: 
    - 编程
    - segmentfault - 频道
author: segmentfault - 频道
comments: false
date: 2021-03-21 16:40:59
thumbnail: https://segmentfault.com/img/remote/1460000039683059
---

<div>   
<p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039683059" alt title referrerpolicy="no-referrer"></span></p><p>MJML是一种现代的电子邮件工具，使开发人员可以在所有设备和邮件客户端上创建美观、响应迅速的出色电子邮件。这种标记语言是为了减少编写响应式电子邮件的痛苦而设计的。</p><p>它的语义语法使其易于使用。它还具有功能丰富的标准组件，可缩短开发时间。在本教程中，我们将使用MJML构建漂亮的响应式邮件，并在多个邮件客户端上进行测试。</p><h2>开始MJML</h2><p>你可以使用npm安装MJML，以将其与Node.js或CLI结合使用：</p><pre><code class="shell">$ npm install -g mjml</code></pre><h2>构建我们的电子邮件</h2><p>首先，请创建一个名为 <code>email.mjml</code> 的文件，尽管你也可以选择其他任何名称。创建文件后，我们的响应式电子邮件将分为以下几部分：</p><ul><li>公司header</li><li>图片header</li><li>Email介绍</li><li>栏目部分</li><li>图标</li><li>社交图标</li></ul><h3>栏目</h3><p>这些部分是我们响应式电子邮件的框架。如上所示，我们的电子邮件将分为六个部分，在我们的 <code>email.mjml</code> 文件中：</p><pre><code class="html"><mjml>
  <mj-body>
    <!-- 公司 Header -->
    <mj-section background-color="#f0f0f0"></mj-section>
    <!-- 图片 Header -->
    <mj-section background-color="#f0f0f0"></mj-section>
    <!-- Email 介绍 -->
    <mj-section background-color="#fafafa"></mj-section>
    <!-- 栏目部分 -->
    <mj-section background-color="white"></mj-section>
    <!-- 图标 -->
    <mj-section background-color="#fbfbfb"></mj-section>
    <!-- 社交图标 -->
    <mj-section background-color="#f0f0f0"></mj-section>
  </mj-body>
</mjml></code></pre><p>从上面可以看到，我们正在使用两个MJML组件：<code>mj-body</code> 和 <code>mj-section</code>。<code>mj-body</code> 定义了我们电子邮件的起点，而 <code>mj-section</code> 定义了一个包含其他组件的节。</p><p>对于定义的每个部分，还定义了具有各自十六进制值的 <code>background-color</code> 属性。</p><h3>公司 Header</h3><p>我们电子邮件的此部分仅在中心横幅位置包含我们的公司/品牌名称：</p><pre><code class="html"><!-- 公司 Header -->
<mj-section background-color="#f0f0f0">
  <mj-column>
    <mj-text  font-style="bold"
        font-size="20px"
        align="center"
        color="#626262">
    Central Park Cruise
    </mj-text>
  </mj-column>
</mj-section></code></pre><p><code>mj-column</code> 组件是用来定义一个列。<code>mj-text</code> 组件用于我们的文本内容，并采取字体样式、字体大小、颜色等样式属性。</p><h3>图片 Header</h3><p>在本部分中，我们将有一个背景图片和一段文字，它们应代表我们的公司口号。我们还会有一个号召性用语按钮，指向一个包含更多详细信息的页面。</p><p>要添加图片标题，你必须将该部分的背景颜色替换为 <code>background-url</code>。与第一个标题相似，你将不得不在垂直和水平方向上居中放置文本，padding保持不变。</p><p>按钮的 <code>href</code> 设置按钮的位置。为了让背景在列中呈现全宽，将列宽设置为600px，<code>width=“600px"</code>。</p><p>我们的电子邮件的这一部分将只包含我们的公司/品牌名称的中心横幅位置。</p><pre><code class="html"><!-- Image Header -->
<mj-section background-url="https://ca-times.brightspotcdn.com/dims4/default/2af165c/2147483647/strip/true/crop/2048x1363+0+0/resize/1440x958!/quality/90/?url=https%3A%2F%2Fwww.trbimg.com%2Fimg-4f561d37%2Fturbine%2Forl-disneyfantasy720120306062055"
            background-size="cover"
            background-repeat="no-repeat">
  <mj-column width="600px">
    <mj-text  align="center"
             color="#fff"
             font-size="40px"
             font-family="Helvetica Neue">Christmas Discount</mj-text>
    <mj-button background-color="#F63A4D" href="#">
      See Promotions
    </mj-button>
  </mj-column>
</mj-section></code></pre><p>要使用图像header，我们将向 <code>jms -section</code> 组件添加 <code>background-url</code> 属性，然后使用 <code>background-size</code> 和 <code>background-repeat</code> 属性设置图像的样式。</p><p>对于我们的口号文本块，我们使用 <code>align</code> 属性将文本在水平和垂直方向上居中对齐。你还可以根据需要设置文本颜色，字体大小，字体系列等。</p><p>号召性用语按钮是使用 <code>mj-button</code> 组件实现的。<code>background-color</code> 属性允许我们指定按钮的背景色，然后使用 <code>href</code> 指定链接或页面的位置。</p><h3>Email件介绍</h3><p>简介文字将由标题，主体文字和号召性用语组成。</p><pre><code class="html"><!-- Intro text -->
<mj-section background-color="#fafafa">
  <mj-column width="400px">
    <mj-text font-style="bold"
             font-size="20px"
             font-family="Helvetica Neue"
             color="#626262">Ultimate Christmas Experience</mj-text>
    <mj-text color="#525252">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin rutrum enim eget magna efficitur, eu semper augue semper. Aliquam erat volutpat. Cras id dui lectus. Vestibulum sed finibus lectus, sit amet suscipit nibh. Proin nec commodo purus. Sed eget nulla elit. Nulla aliquet mollis faucibus.
    </mj-text>
    <mj-button background-color="#F45E43" href="#">Learn more</mj-button>
  </mj-column>
</mj-section></code></pre><h3>栏目部分</h3><p>在这封邮件的部分，我们会有两栏：一栏是描述性的图片，二栏是我们的文字块，用来补充第一部分的图片。</p><pre><code class="html"><!-- Side image -->
<mj-section background-color="white">
  <!-- Left image -->
  <mj-column>
    <mj-image width="200px"
              src="https://navis-consulting.com/wp-content/uploads/2019/09/Cruise1-1.png"/>
  </mj-column>
  <!-- right paragraph -->
  <mj-column>
    <mj-text font-style="bold"
             font-size="20px"
             font-family="Helvetica Neue"
             color="#626262">
      Amazing Experiences
    </mj-text>
    <mj-text color="#525252">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
      Proin rutrum enim eget magna efficitur, eu semper augue semper. 
      Aliquam erat volutpat. Cras id dui lectus. Vestibulum sed finibus 
      lectus.
    </mj-text>
  </mj-column>
</mj-section></code></pre><p>左侧的第一列使用 <code>mj-image</code> 组件指定要使用的图像。该图像可以是本地文件，也可以是远程托管的图像（在我们的情况下是这样）。</p><p>右侧的第二列包含两个文本块，一个用于我们的标题，另一个用于主体文本。</p><h3>图标</h3><p>图标部分将分为三列。你还可以添加更多内容，具体取决于你希望电子邮件的外观。</p><pre><code class="html"><!-- Icons -->
<mj-section background-color="#fbfbfb">
  <mj-column>
    <mj-image width="100px" src="https://191n.mj.am/img/191n/3s/x0l.png" />
  </mj-column>
  <mj-column>
    <mj-image width="100px" src="https://191n.mj.am/img/191n/3s/x01.png" />
  </mj-column>
  <mj-column>
    <mj-image width="100px" src="https://191n.mj.am/img/191n/3s/x0s.png" />
  </mj-column>
</mj-section></code></pre><p>每列都有其自己的 <code>mj-image</code> 组件，用于渲染图标图像。</p><h3>社交图标</h3><p>本部分将包含指向我们的社交媒体帐户的图标。</p><pre><code class="html"><mj-section background-color="#e7e7e7">
  <mj-column>
    <mj-social>
      <mj-social-element name="instagram" />
    </mj-social>
  </mj-column>
</mj-section></code></pre><p>MJML带有 <code>mj-social</code> 组件，可轻松用于显示社交媒体图标。在我们的电子邮件中，我们使用了 Twitter <code>mj-social-element</code>。</p><h2>全部放在一起</h2><p>至此，我们已经实现了所有部分，完整的 <code>email.mjml</code> 应该如下所示：</p><pre><code class="html"><mjml>
  <mj-body>
    <!-- Company Header -->
    <mj-section background-color="#f0f0f0">
      <mj-column>
        <mj-text  font-style="bold"
                 font-size="20px"
                 align="center"
                 color="#626262">
          Central Park Cruises
        </mj-text>
      </mj-column>
    </mj-section>
    <!-- Image Header -->
    <mj-section background-url="https://ca-times.brightspotcdn.com/dims4/default/2af165c/2147483647/strip/true/crop/2048x1363+0+0/resize/1440x958!/quality/90/?url=https%3A%2F%2Fwww.trbimg.com%2Fimg-4f561d37%2Fturbine%2Forl-disneyfantasy720120306062055"
                background-size="cover"
                background-repeat="no-repeat">
      <mj-column width="600px">
        <mj-text  align="center"
                 color="#fff"
                 font-size="40px"
                 font-family="Helvetica Neue">Christmas Discount</mj-text>
        <mj-button background-color="#F63A4D" href="#">
          See Promotions
        </mj-button>
      </mj-column>
    </mj-section>
    <!-- Email Introduction -->
    <mj-section background-color="#fafafa">
      <mj-column width="400px">
        <mj-text font-style="bold"
                 font-size="20px"
                 font-family="Helvetica Neue"
                 color="#626262">Ultimate Christmas Experience</mj-text>
        <mj-text color="#525252">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin rutrum enim eget magna efficitur, eu semper augue semper. Aliquam erat volutpat. Cras id dui lectus. Vestibulum sed finibus lectus, sit amet suscipit nibh. Proin nec commodo purus. Sed eget nulla elit. Nulla aliquet mollis faucibus.
        </mj-text>
        <mj-button background-color="#F45E43" href="#">Learn more</mj-button>
      </mj-column>
    </mj-section>
    <!-- Columns section -->
    <mj-section background-color="white">
      <!-- Left image -->
      <mj-column>
        <mj-image width="200px"
                  src="https://navis-consulting.com/wp-content/uploads/2019/09/Cruise1-1.png"/>
      </mj-column>
      <!-- right paragraph -->
      <mj-column>
        <mj-text font-style="bold"
                 font-size="20px"
                 font-family="Helvetica Neue"
                 color="#626262">
          Amazing Experiences
        </mj-text>
        <mj-text color="#525252">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
          Proin rutrum enim eget magna efficitur, eu semper augue semper. 
          Aliquam erat volutpat. Cras id dui lectus. Vestibulum sed finibus 
          lectus.
        </mj-text>
      </mj-column>
    </mj-section>
    <!-- Icons -->
    <mj-section background-color="#fbfbfb">
      <mj-column>
        <mj-image width="100px" src="https://191n.mj.am/img/191n/3s/x0l.png" />
      </mj-column>
      <mj-column>
        <mj-image width="100px" src="https://191n.mj.am/img/191n/3s/x01.png" />
      </mj-column>
      <mj-column>
        <mj-image width="100px" src="https://191n.mj.am/img/191n/3s/x0s.png" />
      </mj-column>
    </mj-section>
    <!-- Social icons -->
    <mj-section background-color="#e7e7e7">
      <mj-column>
        <mj-social>
          <mj-social-element name="instagram" />
        </mj-social>
      </mj-column>
    </mj-section>
  </mj-body>
</mjml></code></pre><h2>运行我们的应用程序</h2><p>现在我们已经完成了电子邮件的构建，我们可以继续对其进行编译以查看其外观。为此，我们在终端中键入以下内容：</p><pre><code class="shell">mjml -r email.mjml -o .</code></pre><ul><li><code>-r</code>：允许MJML读取和编译我们的 <code>mjml</code> 文件</li><li><code>-o .</code>：告诉MJML将编译后的 <code>mjml</code> 输出保存到同一目录中</li></ul><p>MJML完成编译后，你现在应该在同一目录中看到一个 <code>email.html</code> 文件。 使用你喜欢的电子邮件客户端或浏览器打开它，它的外观应类似于下图：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039683058" alt title referrerpolicy="no-referrer"></span></p><h2>总结</h2><p>正如我们刚才看到的，MJML帮助我们生成跨多个浏览器和客户机响应的高质量、漂亮的HTML电子邮件。</p><hr><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcKH67" alt="image" title="image" referrerpolicy="no-referrer"></span></p>  
</div>
            