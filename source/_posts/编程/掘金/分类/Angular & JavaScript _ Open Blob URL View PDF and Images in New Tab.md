
---
title: 'Angular & JavaScript _ Open Blob URL View PDF and Images in New Tab'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/undefined'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 22:31:05 GMT
thumbnail: 'https://juejin.cn/post/undefined'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/" ref="nofollow noopener noreferrer">August 31, 2020</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fauthor%2Fadmin%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/author/admin/" ref="nofollow noopener noreferrer">Jolly.Exe</a></p>
<p>In this JavaScript quick tutorial, we’ll learn how to select a file using a File input control to convert it into a Base64 URL, also add a View button to preview the selected file by opening in the new Chrome tab by creating a BLOB url.</p>
<p>Article compatible with Angular version starting 4+ up to latest version including 6,7,8,9,10,11 and 12.</p>
<p>In the HTML forms, where we have upload document or image functionality, we usually convert the selected file into a Base64 encoded url to upload it as a string to the remote server, where the base64 string is converted into a file and saved on remote disk space.</p>
<p>We have already discussed how to convert the selected file into a Base64 string URL <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-input-file-image-file-upload-to-base64-tutorial-by-example%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-input-file-image-file-upload-to-base64-tutorial-by-example/" ref="nofollow noopener noreferrer">here</a>, you can check the complete tutorial in Angular.</p>
<p>While filling and selecting the files into form, we may need to provide a preview link using which we can display the selected file to the user in a new browser tab. This can be easily done on the Client-end by converting the File into a Blob object URL.</p>
<p><strong>Summary of content</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23What_is_Blob" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#What_is_Blob" ref="nofollow noopener noreferrer">1) What is Blob?</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23Adding_a_Form" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#Adding_a_Form" ref="nofollow noopener noreferrer">2) Adding a Form</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23Adding_JavaScript" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#Adding_JavaScript" ref="nofollow noopener noreferrer">3) Adding JavaScript</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23Create_a_Blob_URL" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#Create_a_Blob_URL" ref="nofollow noopener noreferrer">3.1) # Create a Blob URL</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23Final_onchange_function" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#Final_onchange_function" ref="nofollow noopener noreferrer">4) Final onchange function</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23Angular_Application" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#Angular_Application" ref="nofollow noopener noreferrer">5) Angular Application</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23Dealing_with_Unsafe_URLs_in_Angular" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#Dealing_with_Unsafe_URLs_in_Angular" ref="nofollow noopener noreferrer">6) Dealing with Unsafe URL’s in Angular</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23Make_Unsafe_URLs_Trusted" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#Make_Unsafe_URLs_Trusted" ref="nofollow noopener noreferrer">7) Make Unsafe URLs Trusted</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23Conclusion" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#Conclusion" ref="nofollow noopener noreferrer">8) Conclusion</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freakyjolly.com%2Fangular-javascript-open-blob-url-view-pdf-and-images-in-new-tab%2F%23Related_Popular_Tutorials" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freakyjolly.com/angular-javascript-open-blob-url-view-pdf-and-images-in-new-tab/#Related_Popular_Tutorials" ref="nofollow noopener noreferrer">9) Related Popular Tutorials</a></p>
<p>We’ll create a sample for a simple JavaScript application and Angular as well. In Angular application, we face unsafe link scenarios which can be resolved by URL sanitization.</p>
<p> </p>
<h2 data-id="heading-0">What is Blob?</h2>
<p>Binary Large Object(Blob) is an Object used to store or holding data in a browser. Blobs can be used to read then save data on disk.</p>
<p>A Blob object has properties to represent the size and MIME type of stored file. This can be used as a normal file.</p>
<p> </p>
<h2 data-id="heading-1">Adding a Form</h2>
<p>Let’s create a simple HTML form with input control of type <code>file</code>. This file control is having a change event handler to convert the selected file into a base64 string. The <code>onchange</code> event will take care to convert the file into base64 anf Blog.</p>
<pre><code class="copyable"><form onsubmit="myFunction(event)">

    <label>Select a File</label>
    <input type="file" name="myfile" onchange="fileChangeEvent(event)">
    <div id="selected-file">
    </div>
    <button>Upload</button>

</form>
Copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h2 data-id="heading-2">Adding JavaScript</h2>
<p>Now add the <code>fileChangeEvent()</code> function which will do the main task for fetching the Base64 URL and Blob based URL.</p>
<p>The <code>FileReader()</code> function is used to read files and then load in the browser’s memory. It returns a callback method <code>onload</code>inside of which we’ll get selected file information.</p>
<pre><code class="copyable">function fileChangeEvent(fileInput) &#123;

  if (fileInput.target.files && fileInput.target.files[0]) &#123;
    const reader = new FileReader();
    reader.onload = (e) => &#123;
      
        ....
        ....

    &#125;;
    reader.readAsDataURL(fileInput.target.files[0]);
  &#125;
&#125;
Copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Inside the <code>reader.onload</code>, we’ll get  <strong>Base64</strong> encoded string URL</p>
<pre><code class="copyable">// Base64 String
console.log(e.target.result);
Copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p>Ad by Valueimpression</p>
<h4 data-id="heading-3"># Create a Blob URL</h4>
<p>To create a Blob we call <code>new Blob()</code>then call <code>window.URL.createObjectURL()</code> to convert it into a URL.</p>
<pre><code class="copyable">// Create a Blog object for selected file & define MIME type
var blob = new Blob(fileInput.target.files, &#123; type: fileInput.target.files[0].type &#125;);

// Create Blog URL 
 var url = window.URL.createObjectURL(blob);
Copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h2 data-id="heading-4">Final <code>onchange</code> function</h2>
<p>After the file is selected by a user, we’ll append the selected <img loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"> inside the </p><div id="user-content-”selected-file”"></div> by using the Javascript, in case of an Image(Png, Jpeg or Gif).<p></p>
<pre><code class="copyable">function fileChangeEvent(fileInput) &#123;

  if (fileInput.target.files && fileInput.target.files[0]) &#123;

    const reader = new FileReader();
    reader.onload = (e) => &#123;
      
      // Create a Blog object for selected file & define MIME type
      var blob = new Blob(fileInput.target.files, &#123; type: fileInput.target.files[0].type &#125;);

      // Create Blog URL 
      var url = window.URL.createObjectURL(blob);

      var element = document.getElementById("selected-file");

      if (
        fileInput.target.files[0].type === 'image/png' ||
        fileInput.target.files[0].type === 'image/gif' ||
        fileInput.target.files[0].type === 'image/jpeg'
      ) &#123;
        // View Image using Base64 String
        console.log(e.target.result);
        var img = document.createElement("img");
        img.src = e.target.result;
        element.appendChild(img);
      &#125;

      // Create Blog View Link
      var a = document.createElement("a");
      var linkText = document.createTextNode("View File");
      a.target = "_blank";
      a.appendChild(linkText);
      a.href = url;
      element.appendChild(a);

    &#125;;
    reader.readAsDataURL(fileInput.target.files[0]);

  &#125;
&#125;
Copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>That’s it the <code><a/></code> tag we are creating above is having the <code>href</code> value assigned with blog <code>url</code>.</p>
<p> </p>
<h2 data-id="heading-5">Angular Application</h2>
<p>For an Angular application, we just need to assign the blob <code>url</code> in the <a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"> tag</a></p><a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">
<pre><code class="copyable"><a class="view-btn-attach" [href]="selectedFileBLOB" target="_blank">View</a>
Copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>But we <strong>can’t</strong> simply assign the url to the selectedFileBLOB as shown below:</p>
<pre><code class="copyable">...
let blob = new Blob(fileInput.target.files, &#123; type: fileInput.target.files[0].type &#125;);
let url = window.URL.createObjectURL(blob);

this.selectedFileBLOB = url;
...
Copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h2 data-id="heading-6">Dealing with Unsafe URL’s in Angular</h2>
<p>Now if you see the HTML template, it will show something like this:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f86159c1f08644cebefaf69be24a414c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Due to security reasons, the non-sanitized dynamic links are automatically marked as Unsafe by Angular.</p>
<p>To resolve this we need to deliberately set them as trusted url by using the  <code>DomSanitizer</code> class.</p>
<p> </p>
<h2 data-id="heading-7">Make Unsafe URLs Trusted</h2>
<p>The <code>bypassSecurityTrustUrl()</code> method provided by the <code>DomSanitizer</code> class.</p>
<pre><code class="copyable">...
import &#123; DomSanitizer &#125; from '@angular/platform-browser';

...
export class AppComponent implements OnInit &#123;


  constructor(
    private sanitizer: DomSanitizer
  ) &#123;&#125;

  ngOnInit() &#123;
  
  &#125;

  
  fileChangeEvent(fileInput: any) &#123;

    if (fileInput.target.files && fileInput.target.files[0]) &#123;

      const reader = new FileReader();
      reader.onload = (e: any) => &#123;
        
let blob = new Blob(fileInput.target.files, &#123; type: fileInput.target.files[0].type &#125;);
        let url = window.URL.createObjectURL(blob);

        this.selectedFileBLOB = this.sanitizer.bypassSecurityTrustUrl(url);

      &#125;;
      reader.readAsDataURL(fileInput.target.files[0]);

    &#125;
  &#125;


&#125;
Copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>This will make passes URL as trusted and used by the user to view the blob url in the new tab.</p></a></div>  
</div>
            