# ezlog: Easy Monitoring of A Log File Generated by NumPyro/NUTS


Oh, you run your NUTS on a distant server?

You can check the NUTS status using this funky code.


## How to Use
```
pip install terminalplot
nohup python -u fit.py >& log & 
python monitor_log.py log
```

## Output in the terminal
```
# STEP ############################################
      **************** **********  * *       *****                                                                      *                             
                                                                                                                                                      
      *                                                                                                                                               
      *                                                                                                                                               
                                                                                                                                                      
    *                              *                                                                                                                  
                                                              *                                                                                       
       *                                                                                                                                              
                                                                                                                                                      
       ********************************************************************************************************************************************** 
                            *                                                                                                          *    **        
     *  * *            *            *                                                          *         *  *         *        * * **   *             
                                  *                             **                                       *                                       *    
     * **** *********** ************************************************************************ *****************************************************
                      ** *                  *                                                                                                         
    **       *  * **  ****** *  ***** * * *** *       *      *    **       **   *    *    **                   *     **      *             **  *   ** 
******** *** ******************** ****   ** *****                                                                                      *              

Min x: 0 Max x: 1500 Min y: 1 Max y: 1023
# TIME (sec) ######################################
      *                                                                                                                                               
      *                                                                                                                                               
         *  *                                                                                                                                         
      **   **  *        *                                                                                                                             
      **** *** **                            *                                                                                                        
       *** ******  *    *    *  *            * *                                                                                                      
      **** ****  *  *  ***   *  *            *** *                                                                                                    
      ** **** ***** *  * *   ** *            *** *                                                                      *                             
        * **** *** ***  ****** **  *  *        *** ***   *** * ***  *** * **   * **  **  *  *** ** ** * * *    ****** ******** ** ** ** ***    *****  
      **  ** ********************* **** * * ***************************************** ** ******* **************************************************** 
        **** * ** ******* ***** ** ************ ******************************* **************** ***************************************  ************
          *   *** ** *** *** ** **************** ** * ** *   ** * **** * * *  * *  ********* ***  ** * ***  ** **   ** ***** *  *****  *   ***** * ** 
    *        *   ***  * ***** ** ** * * ** **   *     *              *              **  * *        *                                                * 
    **           *   *** **       ****   *** ** *                                                                                                     
     *                         *                                                                                                                      
    **                                                                                                                                                
*****                                                                                                                                                 

Min x: 0 Max x: 1500 Min y: 1.06 Max y: 162.86
# TIME/STEP (sec) ############################################
              *                                                                                                                                       
                        *                                                                                                                             
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                            *                                                                                                         
                                                                                                                                                      
                                                                                                                                                      
          *                                                                                                                                           
                                                                                                                                                      
                                                                                                                                                      
      *           *          *                 *                                                                                                      
             * *   *        * *                                                                                                                       
*    * *  **  *    *           *   **        *                                                                                                        
*        *      * *    ****  * *  ** *    *  ** *                                                                                                     
******************************************************************************************************************************************************

Min x: 0 Max x: 1500 Min y: 0.0588135593220339 Max y: 73.71
# summary ######################################
Total steps: 608189
# of chain: 1501
median/chain: 511.0 |min-max 1 - 1023



total time= 29.916 h /  1795.0 min
```
