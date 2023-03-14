import React from 'react'
import {motion} from 'framer-motion'
import {styles} from '../styles'
import { ComputersCanvas } from './canvas'
import { personalInfo} from '../constants/index'


const Hero = () => {
  return (
    <section className = "relative w-full h-screen mx-auto">
      <div className = {`${styles.paddingX} absolute inset-0 top-[120px] max-w-7xl mx-auto flex
      flex-row items-start gap-5`}>
        <div className = "flex flex-col justify-center items-center mt-5">
          <div className = "w-5 h-5 rounded-full bg-[#915eff]"/>
          <div className = "w-1 sm: h-80 h-40 violet-gradient"/>
        </div>
        <div>
            <h1 className = {`${styles.heroHeadText} text-white`}>Hi, I'm <span className = "text-[#915eff]">Harish</span></h1>
            <p className = "mt-2">
              <span>A multi-potentialist, constantly inspired by one's life story - the uncomfortable, the uncertain and the complexity of it all.</span>
              <br />
              <div className = "mt-5">
              <span className = "text-lg text-[#FF6010]">Colorful</span>
              <span className = "text-[#FEB848]">&nbsp; - &nbsp;</span> 
              <span className = "text-lg text-[#286824]">Playful</span>
              <span className = "text-[#9F2B68]">&nbsp; - &nbsp;</span> 
              <span className = "text-lg text-[#784A95]">Emotional</span>
              <br />
              <span className ="text-xs">but most importantly.</span>
              <br />
              <span className = "text-xs">.&nbsp;.&nbsp;.&nbsp;&nbsp;</span>
              <span className = "text-2xl italic font-serif">meaningful</span>
              </div>
            </p>
        </div>
      </div>
      {/* <ComputersCanvas /> */}
      
      <img src ="src\assets\Victory-powerdesign (1).png" 
          className = "w-[300px] h-[400px] absolute rotate-12 top-[60%] left-[80%] md:left-[60%] transform -translate-x-1/2 -translate-y-1/2 z-[0] hover:scale-110 transition-all duration-500 ease-in-out"
      />
      <div className = "absolute xs:bottom-10 bottom-32 w-full flex justify-center items-center">
        <a href = "#about">
          <div className = "w-[35px] h-[64px] rounded-3xl border-4 border-secondary flex justify-center items-start p-2">
            <motion.dev 
              animate = {{
                y: [0, 24, 0]
              }}
              transition = {{
                duration: 1.5,
                repeat: Infinity,
                repeatType: 'loop'
              }}
              className = "w-3 h-3 rounded-full bg-secondary mb-1"
            />
          </div>
        </a>
      </div>

    </section>
  )
}

export default Hero