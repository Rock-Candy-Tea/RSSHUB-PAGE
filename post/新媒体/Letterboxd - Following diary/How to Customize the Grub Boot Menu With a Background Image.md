
---
title: How to Customize the Grub Boot Menu With a Background Image
categories: 
    - 新媒体
    - Letterboxd - Following diary
author: Letterboxd - Following diary
comments: false
date: Sun, 21 Mar 2021 20:00:00 GMT
thumbnail: 'https://track.mailerlite.com/webforms/o/2384299/r3i1n7?v1595538294'
---

<div>   
<p>
            Want to change the background image for the Grub bootloader? Maybe you got bored of the solid black background and now you want to add an attractive image to your boot menu.
    </p>


    


                            
                    
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                                            <!-- No winner found for: mid intro -->
                                                                        
                                
                                                



            
                        <p>
            Here's how you can easily change the Grub background on your Linux machine.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                <!-- No winner found for: native in content -->
                                
            
                        <h2 id="how-to-change-grub-background">
                    How to Change Grub Background</h2>

                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            Most of the Linux users are unaware of the fact that the Grub bootloader can be customized according to their needs. You can change the boot order, modify the background color, and add a new image to the boot menu as well.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            There are several ways to modify the background image in Grub. You can do it by either using your system's file manager or via the command-line.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            But before getting practical, there are some things that you should know. The image that you are going to use as the background should be either of the following extensions: PNG, JPG, and TGA.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                                                                                                                                                
            
                                                                                                
                                
                                                



            
                        <p>
            Also, the JPG/JPEG images should be 8-bit (256 colors) non-indexed files. It's better to stick to a PNG image if you don't want to mess around with bits and image indexing.
    </p>


    


                
                    
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
            
                        <h3 id="change-background-via-command-line">Change Background via Command-Line</h3>
                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            The Grub configuration file or <strong>grub.cfg</strong> is stored in the <strong>/etc/default</strong> folder. You can edit the file using <strong>gedit</strong>, a command-line tool that lets you edit important system files on your computer with minimal risks.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            To change the Grub boot menu background through the terminal:
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
            
                            <ol>
                    <li>
                        Copy the path to the image file.
            </li>
                    <li>
                        Open the <strong>grub.cfg</strong> file located in <strong>/etc/default</strong>.
                                <pre><code class="hljs ">gedit /etc/default/grub.cfg</code></pre>

            </li>
                    <li>
                        Append the following line to the file. Note that you must replace the <strong>/path-to-image</strong> with the path that you have just copied.
                                <pre><code class="hljs ">GRUB_BACKGROUND=/path-to-image</code></pre>

            </li>
                    <li>
                        Save the file and close the editor.
            </li>
                    <li>
                        Update Grub with the new configuration file.
                                <pre><code class="hljs ">sudo update-grub</code></pre>

            </li>
            </ol>

                
                        
            
        
            
            
                                                                                                                                                                                                                                                                                                                                                                
            
                                                                                                
                                
                                                



            
                        <p>
            You will see an output that will look something like this. Note that the second line will confirm if Grub has detected the background image or not.
    </p>


    


                
                    
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
            
                        <pre><code class="hljs ruby">Generating grub.cfg …<br>Found background image: ~/Pictures/yourpicture.png<br>Found linux image: /boot/vmlinuz-2.6.39-0-generic<br>Found initrd image: /boot/initrd.img-2.6.39-0-generic<br>Found linux image: /boot/vmlinuz-2.6.38-8-generic<br>Found initrd image: /boot/initrd.img-2.6.38-8-generic<br>Found memtest86+ image: /boot/memtest86+.bin<br>done</code></pre>

                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            Reboot your system and check if the background image was successfully changed.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
            
                        <h3 id="modify-grub-background-using-a-file-manager">Modify Grub Background Using a File Manager</h3>
                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            Those who are not comfortable with the terminal can use any <a href="https://www.makeuseof.com/linux-file-managers/">Linux file manager</a> to change the Grub background image.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                                                                                                                                                
            
            
                            <ol>
                    <li>
                        Open the default file manager on your system as a root user.
            </li>
                    <li>
                        Copy the image file that you want to use as the background image.
            </li>
                    <li>
                        Paste the file under <strong>/boot/grub</strong> directory.
            </li>
                    <li>
                        Update grub to ensure that the changes are configured.
                                <pre><code class="hljs ">sudo update-grub</code></pre>

            </li>
                    <li>
                        Check to see if Grub has detected the background image or not.
            </li>
            </ol>

                
                    
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
            
                        <pre><code class="hljs ruby">Generating grub.cfg …<br>Found background image: ~/Pictures/yourpicture.png<br>Found linux image: /boot/vmlinuz-2.6.39-0-generic<br>Found initrd image: /boot/initrd.img-2.6.39-0-generic<br>Found linux image: /boot/vmlinuz-2.6.38-8-generic<br>Found initrd image: /boot/initrd.img-2.6.38-8-generic<br>Found memtest86+ image: /boot/memtest86+.bin<br>done</code></pre>

                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            If you paste multiple images to the <strong>/boot/grub</strong> directory, then grub will load the first image and ignore the rest. You can <a href="https://www.makeuseof.com/copy-files-linux-cp/">copy the files using the cp command</a> as well.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            Note that your system will not allow you to paste the image file in the <strong>/boot/grub</strong> folder unless you launch the file manager as a superuser. You can open any Linux application as a root user by typing the following in your terminal.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
            
                        <pre><code class="hljs ">sudo file-manager-name</code></pre>

                
                        
            
        
            
            
                                                                                                                                                                                                                                                                                                                                                                
            
                                                                                                
                                
                                                



            
                        <p>
            For example, if you are using the GNOME desktop environment on Ubuntu Linux, then Nautilus will be your default file manager. To launch Nautilus as a root user:
    </p>


    


                
                    
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
            
                        <pre><code class="hljs ">sudo nautilus</code></pre>

                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                    <div class="ad-even">
                                <!-- No winner found for: every images #0 -->
                            </div>
                                                                                        
            
                        <h2 id="customizing-grub-bootloader-on-linux">
                    Customizing Grub Bootloader on Linux</h2>

                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            You can customize the Grub bootloader by simply editing the <strong>/etc/default/grub.cfg</strong> file. Grub allows users to tweak even the slightest of details in the boot menu.
    </p>


    


                
                        
            
        
            
            
                                                                                                                                                                                                                                    
            
                                                                                                
                                
                                                



            
                        <p>
            For beginners, Linux might be a bit hard to adapt to. Even the installation seems a bit complicated for the first time. Dual-booting multiple operating systems on a computer comes with a risk factor that every novice should know about.
    </p>


    


                
                        
            
                <div id="article-waypoint"></div>
                            
        



        
                                                                                                                                                                                                                                                                                                                                                                        
        
                    
        
        
        <!-- No winner found for: above next button -->

        
                    
    
                
                        


        
                        


        <!-- No winner found for: below next button -->
        <!-- No winner found for: below sharing options -->

                        
    <strong class="section-sub-title">About The Author</strong>
    

                
            
    
    <img src="https://track.mailerlite.com/webforms/o/2384299/r3i1n7?v1595538294" width="1" height="1" style="max-width:1px;max-height:1px;visibility:hidden;padding:0;margin:0;display:block" alt="." border="0" referrerpolicy="no-referrer">
    

                  
</div>
            